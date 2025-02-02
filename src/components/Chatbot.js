import React, { useState, useEffect } from "react";
import { sendChatbotMessage, fetchChatbotMessages } from "../api";

const Chatbot = () => {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState("");

    useEffect(() => {
        fetchChatbotMessages().then(response => setMessages(response.data));
    }, []);

    const handleSendMessage = async () => {
        if (input.trim() === "") return;
        const userMessage = { user: "User", message: input };
        setMessages([...messages, userMessage]);

        try {
            const response = await sendChatbotMessage(input);
            const botResponse = { user: "Bot", message: response.data.response };
            setMessages([...messages, userMessage, botResponse]);
        } catch (error) {
            console.error("Chatbot error:", error);
        }

        setInput("");
    };

    return (
        <div className="p-5 border rounded w-1/2 mx-auto">
            <h2 className="text-xl font-bold">Chatbot Assistant</h2>
            <div className="h-64 overflow-y-auto border p-2">
                {messages.map((msg, index) => (
                    <div key={index} className={`p-2 ${msg.user === "User" ? "text-right" : "text-left"}`}>
                        <strong>{msg.user}:</strong> {msg.message}
                    </div>
                ))}
            </div>
            <div className="mt-3">
                <input 
                    type="text" 
                    value={input} 
                    onChange={(e) => setInput(e.target.value)} 
                    className="border p-2 w-full"
                    placeholder="Type a message..."
                />
                <button onClick={handleSendMessage} className="bg-blue-500 text-white p-2 w-full mt-2">Send</button>
            </div>
        </div>
    );
};

export default Chatbot;
