import { useEffect, useMemo, useState } from 'react';
import Header from './components/Header.jsx';
import Sidebar from './components/Sidebar.jsx';
import PositionCard from './components/PositionCard.jsx';
import EmployeeSearch from './components/EmployeeSearch.jsx'
import * as api from './services/positionsApi.js';
import AddPositionModal from './components/AddPositionModal.jsx';

export default function App() {
  const [activeTab, setActiveTab] = useState('positions');
  const [positions, setPositions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [query, setQuery] = useState('');
  const [onlyActive, setOnlyActive] = useState(false);
  const [showAddModal, setShowAddModal] = useState(false);

  useEffect(() => {
    if (activeTab === 'positions') {
      let ignore = false;
      setLoading(true);
      api.list().then((data) => {
        if (!ignore) {
          setPositions(data);
          setLoading(false);
        }
      });
      return () => { ignore = true; };
    } else {
      setLoading(false);
    }
  }, [activeTab]);

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

  const handleSavePosition = async (newItem) => {
  setPositions(prev => [newItem, ...prev]);
  };

  const handleOpenAdd = () => setShowAddModal(true);
  const handleCloseAdd = () => setShowAddModal(false);

  const renderContent = () => {
    switch (activeTab) {
      case 'positions':
        return (
          <>
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

            <button className="fab" title="Добавить позицию" onClick={handleOpenAdd}>+</button>
            <AddPositionModal
              open={showAddModal}
              onClose={handleCloseAdd}
              onSave={handleSavePosition}
            />
          </>
        );
      
      case 'search':
        return <EmployeeSearch />;
      
      default:
        return <div>Контент не найден</div>;
    }
  };
  return (
    <div className="app">
      <Sidebar activeTab={activeTab} setActiveTab={setActiveTab} />
      <main className="main">
        <Header
          query={query}
          setQuery={setQuery}
          onlyActive={onlyActive}
          setOnlyActive={setOnlyActive}
          showFilters={activeTab === 'positions'}
        />
        
        {renderContent()}
      </main>
    </div>
  );
}