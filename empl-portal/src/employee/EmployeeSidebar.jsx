import { NavLink } from 'react-router-dom';

export default function EmployeeSidebar() {
  const linkCls = ({ isActive }) => 'emp-navlink' + (isActive ? ' active' : '');
  return (
    <nav>
      <div className="emp-menu-title">Меню</div>
      <ul className="emp-menu">
        <li><NavLink className={linkCls} to="/employee/profile">Профиль</NavLink></li>
        <li><NavLink className={linkCls} to="/employee/level">Уровень</NavLink></li>
        <li><NavLink className={linkCls} to="/employee/ai-chat">Чат с ИИ</NavLink></li>
        <li><NavLink className={linkCls} to="/employee/settings">Настройки</NavLink></li>
      </ul>
    </nav>
  );
}