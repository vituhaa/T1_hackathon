import { useState } from 'react';
import Modal from './Modal.jsx';

export default function AddPositionModal({ open, onClose, onSave }) {
  const [title, setTitle] = useState('');
  const [desc, setDesc] = useState(''); // Отдельное состояние для описания
  const [status, setStatus] = useState('open');
  const [tags, setTags] = useState('');
  const [candidates, setCandidates] = useState(0);
  const [saving, setSaving] = useState(false);

  const reset = () => {
    setTitle('');
    setDesc(''); // Сброс описания
    setStatus('open');
    setTags('');
    setCandidates(0);
  };

  const submit = async (e) => {
    e.preventDefault();
    if (!title.trim() || saving) return;
    setSaving(true);
    try {
      const data = {
        id: crypto.randomUUID(),
        title: title.trim(),
        desc: desc.trim(), // Добавляем описание в данные
        status,
        candidates: Number(candidates) || 0,
        tags: tags
          .split(',')
          .map(t => t.trim())
          .filter(Boolean),
        pinned: false
      };
      await onSave?.(data);
      reset();
    } finally {
      setSaving(false);
      onClose?.();
    }
  };

  return (
    <Modal open={open} onClose={onClose} title="Добавить позицию">
      <form className="modal-body" onSubmit={submit}>
        <div className="field">
          <label>Название позиции</label>
          <input
            className="input"
            placeholder="Например: Python-разработчик"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />
        </div>

        <div className="field">
          <label>Описание</label>
          <input
            className="input"
            placeholder="Обозначьте суть работы и обязанности сотрудника"
            value={desc} // Исправлено: используем состояние desc
            onChange={(e) => setDesc(e.target.value)} // Исправлено: обновляем desc
          />
        </div>

        <div className="field">
          <label>Статус</label>
          <select
            className="input"
            value={status}
            onChange={(e) => setStatus(e.target.value)}
          >
            <option value="open">Открытая</option>
            <option value="closed">Закрытая</option>
          </select>
        </div>

        <div className="field">
          <label>Компетенции (через запятую)</label>
          <input
            className="input"
            placeholder="C++, English, DataAnalysis"
            value={tags}
            onChange={(e) => setTags(e.target.value)}
          />
        </div>

        <div className="modal-actions">
          <button type="button" className="btn ghost" onClick={onClose}>
            Отмена
          </button>
          <button type="submit" className="btn primary" disabled={saving || !title.trim()}>
            Сохранить
          </button>
        </div>
      </form>
    </Modal>
  );
}