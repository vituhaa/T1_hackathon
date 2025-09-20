import "../employee.css";

export default function Profile() {
  // демо-данные — потом подставишь реальные с бэка
  const completion = 60;

  return (
    <div className="profile">
      <button className="back-btn" aria-label="Назад">←</button>

      <div className="profile__header">
        <div className="profile__avatar" />
        <div className="profile__meter">
          <div className="profile__meter-fill" style={{height: `${completion}%`}} />
        </div>
      </div>

      <h1 className="profile__name">Имя фамилия</h1>
      <div className="profile__caption">{completion}% Профиля Заполнено!</div>

      <section className="profile-card">
        <div className="profile-card__head">
          <span>Образование</span>
          <a className="link-success" href="#">Обнови данные и получишь +35XP</a>
        </div>
        <div className="profile-card__body">
          Образованный типа
          <div className="muted">Последнее обновление — 01.01.2000</div>
          <button className="link">Редактировать</button>
        </div>
      </section>

      <section className="profile-card">
        <div className="profile-card__head"><span>Текущие роли</span></div>
        <div className="profile-card__body">
          <ul className="list">
            <li>Роль 1</li>
            <li>Роль 2</li>
          </ul>
          <button className="link">Редактировать</button>
        </div>
      </section>

      <section className="profile-card">
        <div className="profile-card__head"><span>Компетенции</span></div>
        <div className="profile-card__body">
          <ul className="tags">
            <li>Python</li>
            <li>C++</li>
          </ul>
          <button className="link">Редактировать</button>
        </div>
      </section>
    </div>
  );
}
