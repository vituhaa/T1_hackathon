import { useState } from 'react';
import EmployeeCard from './EmployeeCard';
export default function PositionCard({ data, onDelete, onTogglePin }) {
  const { title, candidates = 0, status = 'open', tags = [], pinned } = data;
  const [isModalOpen, setIsModalOpen] = useState(false);

  const handleOpen = () => setIsModalOpen(true);
  const handleClose = () => setIsModalOpen(false);

  return (
    <>
    <article className="card">
      <div className="card-left">
        <div className={`status-dot ${status}`} />
      </div>

      <div className="card-main">
        <div className="card-title">
          <span>{title}</span>
          {pinned && <span className="pin">★</span>}
        </div>
        <div className="card-sub">
          <span className="muted">Кандидатов: {candidates}</span>
          <span className="tags">
            {tags.map((t, i) => <span className="tag" key={i}>{t}</span>)}
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
              <h2>{title}</h2>
              <button className="modal-close" onClick={handleClose}>×</button>
            </div>
            <div className="modal-content">
              <p>Здесь будет содержимое позиции</p>
              <div className="employee-section">
          <h3 style={{marginLeft: '8px', marginBottom: '12px', fontSize: '16px', fontWeight: '600'}}>
            Ответственный сотрудник
          </h3>
          <EmployeeCard 
            data={{
              name: "Иванов Иван",
              position: "Senior Recruiter",
              department: "HR отдел",
              experience: 5,
              skills: ["Подбор", "Собеседование", "Onboarding"]
            }}
            onViewDetails={() => console.log("View employee details")}
          />
        </div>
            </div>
            <div className="modal-footer">
              <button className="btn" onClick={handleClose}>Закрыть</button>
            </div>
          </div>
        </div>
      )}
    </>
  );
}