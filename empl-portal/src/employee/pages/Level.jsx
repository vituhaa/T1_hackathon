import "../employee.css";

export default function Level() {
  const level = 4;
  const next = 5;
  const progress = 45; // %

  return (
    <div className="level">
      <button className="back-btn" aria-label="Назад">←</button>

      <div className="level__badge">
        <div className="level__badge-circle">{`Ур. ${level}`}</div>
      </div>

      <h1 className="level__name">Имя фамилия</h1>

      <div className="level__progress">
        <div className="level__progress-bar">
          <div className="level__progress-fill" style={{width: `${progress}%`}} />
        </div>
        <div className="level__progress-next">Ур. {next}</div>
      </div>

      <div className="level__tabs">
        <button className="link">Дорожная карта карьеры</button>
        <div className="level__divider" />
        <span className="muted">Достижения</span>
      </div>

      <div className="level__grid">
        <div className="level__bubble">Проект 1<br/>Роль</div>
        <div className="level__ladder">
          <div className="chip chip--ghost">Стажер</div>
          <div className="chip chip--success">Джун</div>
          <div className="chip chip--dashed">Миддл</div>
        </div>
        <div className="level__bubble">Проект 2<br/>Роль</div>
        <div className="level__bubble">Проект 3<br/>Роль</div>
      </div>
    </div>
  );
}
