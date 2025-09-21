export default function PositionCard({ data, onDelete, onTogglePin }) {
  const { title, candidates = 0, status = 'open', tags = [], pinned } = data;
  return (
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
        <button className="btn ghost">Открыть</button>
        <button className="btn ghost danger" onClick={onDelete}>Удалить</button>
        <button className={`btn ghost ${pinned ? 'pin-on' : ''}`} onClick={onTogglePin}>
          {pinned ? 'Открепить' : 'Закрепить'}
        </button>
      </div>
    </article>
  );
}