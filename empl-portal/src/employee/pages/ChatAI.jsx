import { useEffect, useRef, useState } from "react";
import "../employee.css";

export default function ChatAI() {
  const [messages, setMessages] = useState([
    { id: 1, role: "assistant", text: "Привет! Я помогу с карьерой и компетенциями." }
  ]);
  const [input, setInput] = useState("");
  const scroller = useRef(null);

  useEffect(() => {
    scroller.current?.scrollTo({ top: scroller.current.scrollHeight, behavior: "smooth" });
  }, [messages]);

  async function send() {
    const text = input.trim();
    if (!text) return;
    const userMsg = { id: Date.now(), role: "user", text };
    setMessages(prev => [...prev, userMsg]);
    setInput("");

    // заглушка ответа — тут подключишь свой бэкэнд
    // пример: const res = await fetch("/api/ai/chat", { method:"POST", headers:{'Content-Type':'application/json'}, body: JSON.stringify({ message: text })});
    // const data = await res.json();
    // const botText = data.reply;
    const botText = `Эхо: ${text}`;

    setMessages(prev => [...prev, { id: Date.now()+1, role: "assistant", text: botText }]);
  }

  function onKey(e) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault(); send();
    }
  }

  return (
    <div className="chat">
      <div className="chat__header">Чат с ИИ</div>

      <div ref={scroller} className="chat__messages">
        {messages.map(m => (
          <div key={m.id} className={`bubble bubble--${m.role}`}>
            {m.text}
          </div>
        ))}
      </div>

      <div className="chat__composer">
        <textarea
          value={input}
          onChange={(e)=>setInput(e.target.value)}
          onKeyDown={onKey}
          placeholder="Напишите сообщение..."
          rows={1}
          className="chat__input"
        />
        <button className="chat__send" onClick={send}>Отправить</button>
      </div>
    </div>
  );
}
