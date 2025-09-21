import { useEffect, useRef, useState } from "react";
import "../employee.css";

const MAX_INPUT_HEIGHT = 160; // лимит автовороста textarea

export default function ChatAI() {
  const [messages, setMessages] = useState([
    { id: 1, role: "assistant", text: "Привет! Я помогу с карьерой и компетенциями." }
  ]);
  const [input, setInput] = useState("");
  const scroller = useRef(null);
  const taRef = useRef(null);

  useEffect(() => {
    scroller.current?.scrollTo({ top: scroller.current.scrollHeight, behavior: "smooth" });
  }, [messages]);

const MAX_H = 160;

useEffect(() => {
  const ta = taRef.current;
  if (!ta) return;

  ta.style.height = "auto";
  const h = Math.min(MAX_H, ta.scrollHeight);
  ta.style.height = h + "px";

  const needScroll = ta.scrollHeight > ta.clientHeight + 1; // запас на субпиксели
  ta.classList.toggle("no-scrollbar", !needScroll);
  ta.classList.toggle("has-scroll", needScroll);
}, [input]);



  async function send() {
    const text = input.trim();
    if (!text) return;
    const userMsg = { id: Date.now(), role: "user", text };
    setMessages(prev => [...prev, userMsg]);
    setInput("");

    // заглушка ответа
    const botText = `Эхо: ${text}`;
    setMessages(prev => [...prev, { id: Date.now() + 1, role: "assistant", text: botText }]);
  }

  function onKey(e) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      send();
    }
  }

  return (
    <div className="chat">
      <div className="chat__header">Чат с ИИ</div>

      <div ref={scroller} className="chat__messages">
        {messages.map(m => (
          <div key={m.id} className={`bubble bubble--${m.role}`}>{m.text}</div>
        ))}
      </div>

      <div className="chat__composer">
        <textarea
          ref={taRef}
          value={input}
          onChange={(e)=>setInput(e.target.value)}
          onKeyDown={onKey}
          placeholder="Напишите сообщение..."
          rows={1}
          className="chat__input no-scrollbar" /* по умолчанию без полосы */
        />
        <button className="chat__send" onClick={send}>Отправить</button>
      </div>
    </div>
  );
}
