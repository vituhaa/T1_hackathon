// Заглушка API. Позже можно заменить на:
// export async function list() { const r = await fetch('/api/positions'); return r.json(); }
export async function list() {
  const demo = [
    {
      id: '1',
      title: 'Data Analyst',
      status: 'open',
      candidates: 12,
      tags: ['SQL', 'Tableau', 'Mid'],
      pinned: true
    },
    {
      id: '2',
      title: 'Backend Engineer (Python)',
      status: 'open',
      candidates: 7,
      tags: ['Django', 'PostgreSQL'],
      pinned: false
    },
    {
      id: '3',
      title: 'Product Manager',
      status: 'on_hold',
      candidates: 3,
      tags: ['B2C', 'Growth'],
      pinned: false
    },
    {
      id: '4',
      title: 'QA Engineer',
      status: 'draft',
      candidates: 0,
      tags: ['Автотесты'],
      pinned: false
    }
  ];

  return new Promise((res) => setTimeout(() => res(demo), 400));
}

const API_URL = "http://localhost:5000/api";

export async function getHello() {
  const res = await fetch(`${API_URL}/hello`);
  return res.json();
}

export async function getPositionInfo(pos_id) {
  const res = await fetch(`${API_URL}/position_card/${pos_id}`);
  return res.json();
}

export async function getPositions() {
  const res = await fetch(`${API_URL}/positions`);
  return res.json();
}

