import { NavLink, Outlet } from "react-router-dom";
import "./employee.css";

export default function EmployeeLayout() {
  return (
    <div className="emp-shell">
      <aside className="emp-sidebar">
        <div className="emp-sidebar__title">Меню</div>
        <nav className="emp-nav">
          <NavLink to="profile" className={({isActive}) => "emp-nav__item" + (isActive ? " is-active" : "")}>
            Профиль
          </NavLink>
          <NavLink to="level" className={({isActive}) => "emp-nav__item" + (isActive ? " is-active" : "")}>
            Уровень
          </NavLink>
          <NavLink to="chat" className={({isActive}) => "emp-nav__item" + (isActive ? " is-active" : "")}>
            Чат с ИИ
          </NavLink>
          <NavLink to="settings" className={({isActive}) => "emp-nav__item" + (isActive ? " is-active" : "")}>
            Настройки
          </NavLink>
        </nav>
      </aside>

      <main className="emp-main">
        <Outlet />
      </main>
    </div>
  );
}
