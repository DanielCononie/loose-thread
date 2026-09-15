
import { useChat } from "@ai-sdk/react";
import { useState } from "react";
import { TextStreamChatTransport } from "ai";
import Markdown from "react-markdown";
import remarkBreaks from "remark-breaks";
import { useNavigate } from "react-router-dom";

function Home() {
  const transport = new TextStreamChatTransport({
    api: "http://localhost:8000/api/detective",
  });
  const navigate = useNavigate();

  const [input, setInput] = useState("");
  const { messages, sendMessage } = useChat({ transport });

  return (
    <>
      <form
        onSubmit={(event) => {
          event.preventDefault();
          sendMessage({ text: input });
          setInput("");
        }}
      >
        <input value={input} onChange={(event) => setInput(event.target.value)} />
      </form>
      <button onClick={() => navigate("/open-case")}>Open a Case</button>

      <div>
        {messages.map((message, index) => (
          <div key={index}>
            {message.parts.map((part, partIndex) =>
              part.type === "text" ? (
                <div key={partIndex}>
                  <strong>{message.role}: </strong>
                  <Markdown remarkPlugins={[remarkBreaks]}>{part.text}</Markdown>
                </div>
              ) : null,
            )}
          </div>
        ))}
      </div>
    </>
  );
}

export default Home;
