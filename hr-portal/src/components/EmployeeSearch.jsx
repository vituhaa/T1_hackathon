import EmployeeCard from './EmployeeCard.jsx';

export default function EmployeeSearch() {
  const employees = [
    {
      id: 1,
      name: 'Иван Петров',
      position: 'Frontend Developer',
      department: 'IT отдел',
      experience: 5,
      skills: ['React', 'JavaScript', 'TypeScript', 'Vue']
    },
    {
      id: 2,
      name: 'Мария Сидорова',
      position: 'HR Manager',
      department: 'Отдел кадров',
      experience: 3,
      skills: ['Recruitment', 'Interviews', 'Onboarding']
    },
    {
      id: 3,
      name: 'Алексей Иванов',
      position: 'Backend Developer',
      department: 'IT отдел',
      experience: 7,
      skills: ['Node.js', 'Python', 'PostgreSQL', 'Docker']
    },
    {
      id: 4,
      name: 'Екатерина Смирнова',
      position: 'UI/UX Designer',
      department: 'Дизайн отдел',
      experience: 4,
      skills: ['Figma', 'Adobe XD', 'Illustrator', 'Photoshop']
    },
    {
      id: 5,
      name: 'Дмитрий Кузнецов',
      position: 'Project Manager',
      department: 'Отдел управления',
      experience: 6,
      skills: ['Agile', 'Scrum', 'JIRA', 'Team Leadership']
    },
    {
      id: 6,
      name: 'Ольга Новикова',
      position: 'QA Engineer',
      department: 'IT отдел',
      experience: 4,
      skills: ['Testing', 'Selenium', 'Jest', 'Cypress']
    }
  ];

  const handleViewDetails = (employeeId) => {
    console.log('Открыть подробности сотрудника:', employeeId);
  };

  return (
    <section className="section">
      <div className="section-head">
        <h2>Поиск сотрудников</h2>
        <div className="search" style={{ maxWidth: '300px' }}>
          <span className="search-icon">🔍</span>
          <input 
            type="text" 
            placeholder="Поиск сотрудников..." 
          />
        </div>
      </div>

      <div className="cards">
        {employees.map(employee => (
          <EmployeeCard
            key={employee.id}
            data={employee}
            onViewDetails={() => handleViewDetails(employee.id)}
          />
        ))}
      </div>
    </section>
  );
}