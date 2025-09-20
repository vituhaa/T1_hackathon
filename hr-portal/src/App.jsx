import { useEffect, useMemo, useState } from 'react';
import Header from './components/Header.jsx';
import Sidebar from './components/Sidebar.jsx';
import PositionCard from './components/PositionCard.jsx';
import * as api from './services/positionsApi.js';

export default function App() {
  const [positions, setPositions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [query, setQuery] = useState('');
  const [onlyActive, setOnlyActive] = useState(false);

  useEffect(() => {
    let ignore = false;
    setLoading(true);
    api.list().then((data) => {
      if (!ignore) {
        setPositions(data);
        setLoading(false);
      }
    });
    return () => { ignore = true; };
  }, []);

  const filtered = useMemo(() => {
    let items = positions;
    if (query.trim()) {
      const q = query.toLowerCase();
      items = items.filter(p =>
        p.title.toLowerCase().includes(q) ||
        (p.tags || []).some(t => t.toLowerCase().includes(q))
      );
    }
    if (onlyActive) items = items.filter(p => p.status === 'open');
    return items;
  }, [positions, query, onlyActive]);

  const handleDelete = (id) => {
    setPositions(prev => prev.filter(p => p.id !== id));
  };

  const handleTogglePin = (id) => {
    setPositions(prev => prev.map(p => p.id === id ? { ...p, pinned: !p.pinned } : p));
  };

  const handleAdd = () => {
    const id = crypto.randomUUID();
    setPositions(prev => [
      {
        id,
        title: `Новая позиция ${prev.length + 1}`,
        status: 'draft',
        candidates: 0,
        tags: ['черновик'],
        pinned: false,
      },
      ...prev
    ]);
  };

  return (
    <div className="app">
      <Sidebar />
      <main className="main">
        <Header
          query={query}
          setQuery={setQuery}
          onlyActive={onlyActive}
          setOnlyActive={setOnlyActive}
        />

        <section className="section">
          <div className="section-head">
            <h2>Позиции</h2>

          </div>

          {loading && <div className="skeleton-list">Загрузка...</div>}

          {!loading && filtered.length === 0 && (
            <div className="empty">
              <div className="empty-title">Ничего не найдено</div>
              <div className="empty-sub">Попробуйте изменить запрос</div>
            </div>
          )}

          {!loading && filtered.length > 0 && (
            <div className="cards">
              {filtered
                .sort((a, b) => Number(b.pinned) - Number(a.pinned))
                .map(p => (
                <PositionCard
                  key={p.id}
                  data={p}
                  onDelete={() => handleDelete(p.id)}
                  onTogglePin={() => handleTogglePin(p.id)}
                />
              ))}
            </div>
          )}
        </section>

        <button className="fab" title="Добавить позицию" onClick={handleAdd}>+</button>
      </main>
    </div>
  );
}