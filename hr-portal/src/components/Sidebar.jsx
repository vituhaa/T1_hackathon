export default function Sidebar({ activeTab, setActiveTab }) {
  return (
    <aside className="sidebar">
      <div className="logo">HR Portal</div>
      <nav className="menu">
        <a 
          className={`menu-item ${activeTab === 'positions' ? 'active' : ''}`}
          onClick={() => setActiveTab('positions')}
          style={{ cursor: 'pointer' }}
        >
          Позиции
        </a>
        <a 
          className={`menu-item ${activeTab === 'search' ? 'active' : ''}`}
          onClick={() => setActiveTab('search')}
          style={{ cursor: 'pointer' }}
        >
          Поиск сотрудников
        </a>
      </nav>
    </aside>
  );
}