export default function EmployeeCard({ data, onViewDetails }) {
  const { name, position, department, experience, skills = [] } = data;

  const getInitials = (fullName) => {
    return fullName
      .split(' ')
      .map(word => word.charAt(0))
      .join('')
      .toUpperCase()
      .slice(0, 2);
  };

  return (
    <article className="card">
      <div className="card-left">
        <div className="employee-avatar">
          {getInitials(name)}
        </div>
      </div>

      <div className="card-main">
        <div className="card-title">
          <span>{name}</span>
        </div>
        <div className="card-sub">
          <span className="position">{position}</span>
          {department && <span className="muted">{department}</span>}
          {experience && <span className="muted">Опыт: {experience} лет</span>}
          {skills.length > 0 && (
            <span className="tags">
              {skills.map((skill, i) => (
                <span className="tag" key={i}>{skill}</span>
              ))}
            </span>
          )}
        </div>
      </div>

      <div className="card-actions">
        <button className="btn ghost" onClick={onViewDetails}>
          Подробнее
        </button>
      </div>
    </article>
  );
}