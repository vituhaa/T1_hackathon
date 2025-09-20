export default function Header({ query, setQuery, onlyActive, setOnlyActive }) {
  return (
    <header className="header">
      <div className="search">
        <span className="search-icon">🔎</span>
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Профессия, должность или тэг"
        />
        <button className="btn ghost" onClick={() => setQuery('')}>Очистить</button>
      </div>

      <div className="header-actions">
        <button
          className={`chip ${onlyActive ? 'chip-on' : ''}`}
          onClick={() => setOnlyActive(v => !v)}
        >
          Открытые
        </button>

        <button className="btn primary">Фильтр</button>

        <div className="profile">
          <div className="avatar">HR</div>
          <div className="profile-name">HR-отдел</div>
        </div>
      </div>
    </header>
  );
}