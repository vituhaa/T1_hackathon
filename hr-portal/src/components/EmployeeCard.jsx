import { useState } from 'react';
export default function EmployeeCard({ data, onViewDetails }) {
  const { name, skills = [] } = data;
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
          {skills.length > 0 && (
          <span className="tags">
            {skills.map((skill, i) => (
              <span className="tag" key={i}>
                {skill.name} ({skill.level})
              </span>
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