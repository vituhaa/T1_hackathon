import "../employee.css";

export default function Profile() {
  const filled = 60;

  return (
    <div className="profile profile--stack">
      {/* шапка профиля: слева аватар+метр, справа имя+процент */}
      <div className="profile__header profile__header--row">
        <div className="profile__col profile__col--left">
          <div className="profile__avatar" aria-hidden />
          <div className="profile__meter" aria-label={`Заполнено ${filled}%`}>
            <div className="profile__meter-fill" style={{ height: `${filled}%` }} />
          </div>
        </div>

        <div className="profile__col profile__col--right">
          <h1 className="profile__name">Имя фамилия</h1>
          <div className="profile__caption">{filled}% Профиля Заполнено!</div>
        </div>
      </div>

      {/* карточки — одинакового размера */}
      <div className="profile__stack">
        <section className="profile-card profile-card--equal">
          <div className="profile-card__head">
            <span>Образование</span>
            <button className="link">Обнови данные и получишь +35XP</button>
          </div>
          <div className="profile-card__body">
            <div>Бакалавриат, магистратура, дополнительные курсы</div>
            <button className="link" style={{ position: "static" }}>Редактировать</button>
            <div className="muted">Последнее обновление — 01.01.2000</div>
          </div>
        </section>

        <section className="profile-card profile-card--equal">
          <div className="profile-card__head"><span>Текущие роли</span></div>
          <div className="profile-card__body" style={{ paddingRight: 0 }}>
            <ul className="list">
              <li>Роль 1</li>
              <li>Роль 2</li>
            </ul>
            <button className="link" style={{ position: "static" }}>Редактировать</button>
          </div>
        </section>

        <section className="profile-card profile-card--equal">
          <div className="profile-card__head"><span>Компетенции</span></div>
          <div className="profile-card__body" style={{ paddingRight: 0 }}>
            <ul className="tags">
              <li>Python</li><li>C++</li>
            </ul>
            <button className="link" style={{ position: "static" }}>Редактировать</button>
          </div>
        </section>
      </div>
    </div>
  );
}
