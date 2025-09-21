import { useState } from 'react';
import EmployeeCard from './EmployeeCard';
import { getPositionInfo } from '../services/positionsApi';
export default function PositionCard({ data, onDelete, onTogglePin }) {
  const { id, name, description, created_at, is_closed, skills = [], pinned } = data;
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [position, setPosition] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleOpen = async () => {
    setIsModalOpen(true);
    setLoading(true);
    setError(null);

    try {
      const pos = await getPositionInfo(id);
      setPosition(pos);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };
  const handleClose = () => setIsModalOpen(false);

  return (
    <>
    <article className="card">
      <div className="card-left">
        <div className={`status-dot ${is_closed}`} />
      </div>

      <div className="card-main">
        <div className="card-title">
          <span>{name}</span>
          {pinned && <span className="pin">★</span>}
        </div>
        <div className="card-sub">
          {/* <span className="muted">Кандидатов: {candidates}</span> */}
          <span className="tags">
            {skills.map((t, i) => <span className="tag" key={i}>{t.name}</span>)}
          </span>
        </div>
      </div>

      <div className="card-actions">
        <button className="btn ghost" onClick={handleOpen}>Открыть</button>
        <button className="btn ghost danger" onClick={onDelete}>Удалить</button>
        <button className={`btn ghost ${pinned ? 'pin-on' : ''}`} onClick={onTogglePin}>
          {pinned ? 'Открепить' : 'Закрепить'}
        </button>
      </div>
    </article>

    {isModalOpen && (
        <div className="modal-overlay">
          <div className="modal">
            <div className="modal-header">
              <h2>{name}</h2>
              <button className="modal-close" onClick={handleClose}>×</button>
            </div>
            <div className="modal-content">
              {/* <p>Здесь будет содержимое позиции</p> */}
              {loading && <p>Загрузка...</p>}
              {position && (
                <>
                  <p><strong>Описание:</strong> {position.description}</p>
                  <p><strong>Создано</strong> {position.created_at}</p>
                </>
              )}
              <div className="employee-section">
          <h3 style={{marginLeft: '8px', marginBottom: '12px', fontSize: '16px', fontWeight: '600'}}>
            Подходящие сотрудники
          </h3>
          {Array.isArray(position?.employees) && position.employees.length > 0 ? (
            position.employees.map(emp => (
            <EmployeeCard
              key={emp.id}
              data={emp}
              onViewDetails={() => console.log("View employee", emp.id)}
          />
        ))
        ) : (
        <p>Нет сотрудников</p>)}
        </div>
            </div>
            {/* <div className="modal-footer">
              <button className="btn" onClick={handleClose}>Закрыть</button>
            </div> */}
          </div>
        </div>
      )}
    </>
  );
}