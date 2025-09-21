import "../employee.css";

export default function Level() {
  const level = 4;
  const next = 5;
  const progress = 45; // %

  return (
    <div className="level level--v1">
      {/* бейдж уровня */}
      <div className="level__badge">
        <div className="level__badge-circle">{`Ур. ${level}`}</div>
      </div>

      {/* имя */}
      <h1 className="level__name">Имя фамилия</h1>

      {/* прогресс до след. ур. */}
      <div className="level__progress level__progress--v1">
        <div className="level__progress-next">{`Ур. ${level}`}</div>
        <div className="level__progress-bar">
          <div className="level__progress-fill" style={{ width: `${progress}%` }} />
        </div>
        <div className="level__progress-next">{`Ур. ${next}`}</div>
      </div>

      {/* вкладки/заголовки */}
      <div className="level__tabs level__tabs--v1">
        <button className="link">Дорожная карта карьеры</button>
        <div className="level__tabs-right">
          <span className="level__tabs-title">Достижения</span>
          <span className="level__tabs-divider" />
        </div>
      </div>

      {/* контент: слева проекты, справа лестница */}
      <div className="level__content">
        <div className="level__projects">
          <div className="level__pill">Проект 1<br/>Роль</div>
          <div className="level__pill">Проект 2<br/>Роль</div>
          <div className="level__pill">Проект 3<br/>Роль</div>
        </div>

        <div className="level__ladder level__ladder--v1">
          <div className="chip chip--ghost">Стажер</div>
          <div className="level__arrow" />
          <div className="chip chip--success chip--xl">Джун</div>
          <div className="level__arrow" />
          <div className="chip chip--dashed chip--xl">Миддл</div>
        </div>
      </div>
    </div>
  );
}
