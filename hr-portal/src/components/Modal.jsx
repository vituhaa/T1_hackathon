import { useEffect, useRef } from 'react';
import { createPortal } from 'react-dom';

export default function Modal({ open, onClose, title, children }) {
  const overlayRef = useRef(null);
  const dialogRef = useRef(null);
  const prevFocusRef = useRef(null);
  const titleId = useRef(`modal-title-${Math.random().toString(36).slice(2)}`);

  useEffect(() => {
    if (!open) return;
    prevFocusRef.current = document.activeElement;

    const focusFirst = () => {
      const el = dialogRef.current;
      if (!el) return;
      const focusable = el.querySelectorAll(
        'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
      );
      (focusable[0] || el).focus();
    };

    const onKeyDown = (e) => {
      if (e.key === 'Escape') onClose?.();
    };

    document.addEventListener('keydown', onKeyDown);
    const prevOverflow = document.body.style.overflow;
    document.body.style.overflow = 'hidden';
    setTimeout(focusFirst, 0);

    return () => {
      document.removeEventListener('keydown', onKeyDown);
      document.body.style.overflow = prevOverflow;
      prevFocusRef.current && prevFocusRef.current.focus?.();
    };
  }, [open, onClose]);

  if (!open) return null;

  const onOverlayClick = (e) => {
    if (e.target === overlayRef.current) onClose?.();
  };

  return createPortal(
    <div
      className="modal-overlay"
      ref={overlayRef}
      onMouseDown={onOverlayClick}
    >
      <div
        className="modal"
        role="dialog"
        aria-modal="true"
        aria-labelledby={title ? titleId.current : undefined}
        ref={dialogRef}
      >
        {(title || onClose) && (
          <div className="modal-header">
            <div id={titleId.current} className="modal-title">{title}</div>
            {onClose && (
              <button
                className="btn ghost modal-close"
                aria-label="Закрыть"
                onClick={onClose}
              >
                ×
              </button>
            )}
          </div>
        )}
        {children}
      </div>
    </div>,
    document.body
  );
}