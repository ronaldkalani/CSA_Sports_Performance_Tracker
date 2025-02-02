import React, { useEffect, useState } from "react";
import io from "socket.io-client";
import {
  fetchAssessmentMetrics,
  fetchAthleteGoals,
  fetchChatbotConversations,
  fetchChatbotMessages,
  fetchFeedback,
  fetchMetrics,
  fetchMetricSessions,
  fetchNotifications,
  fetchParticipants,
  fetchSportsLeadershipEvaluations,
} from "../api/api";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from "recharts";
import Chart from "../components/Chart";

const socket = io("http://127.0.0.1:8000", {
  transports: ["websocket"],
  reconnection: true,
});

const Dashboard = () => {
  const [metrics, setMetrics] = useState([]);
  const [goals, setGoals] = useState([]);
  const [chatbotConversations, setChatbotConversations] = useState([]);
  const [chatbotMessages, setChatbotMessages] = useState([]);
  const [feedback, setFeedback] = useState([]);
  const [metricSessions, setMetricSessions] = useState([]);
  const [notifications, setNotifications] = useState([]);
  const [participants, setParticipants] = useState([]);
  const [leadershipEvaluations, setLeadershipEvaluations] = useState([]);
  const [message, setMessage] = useState("");

  useEffect(() => {
    // Fetch API Data
    fetchAssessmentMetrics().then((res) => setMetrics(res.data));
    fetchAthleteGoals().then((res) => setGoals(res.data));
    fetchChatbotConversations().then((res) => setChatbotConversations(res.data));
    fetchChatbotMessages().then((res) => setChatbotMessages(res.data));
    fetchFeedback().then((res) => setFeedback(res.data));
    fetchMetrics().then((res) => setMetrics(res.data));
    fetchMetricSessions().then((res) => setMetricSessions(res.data));
    fetchNotifications().then((res) => setNotifications(res.data));
    fetchParticipants().then((res) => setParticipants(res.data));
    fetchSportsLeadershipEvaluations().then((res) => setLeadershipEvaluations(res.data));

    // WebSocket Live Data
    socket.on("newData", (data) => {
      setMessage(data);
    });

    return () => {
      socket.off("newData");
    };
  }, []);

  return (
    <div className="container mx-auto p-5">
      <h1 className="text-3xl font-bold">Athlete Performance Dashboard</h1>

      {/* WebSocket Live Data */}
      <h2 className="text-xl font-bold mt-5">Live Data</h2>
      <p className="border p-2">{message}</p>

      {/* Assessment Metrics Chart */}
      <h2 className="text-xl font-bold mt-5">Assessment Metrics</h2>
      <LineChart width={800} height={400} data={metrics}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="participant" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="pre_score" stroke="#8884d8" />
        <Line type="monotone" dataKey="post_score" stroke="#82ca9d" />
      </LineChart>

      {/* Athlete Goals */}
      <h2 className="text-xl font-bold mt-5">Athlete Goals</h2>
      <ul>
        {goals.map((g) => (
          <li key={g.id} className="border p-2">
            {g.participant} - {g.goal_description} (Target: {g.target_date})
          </li>
        ))}
      </ul>

      {/* Chatbot Conversations */}
      <h2 className="text-xl font-bold mt-5">Chatbot Conversations</h2>
      <ul>
        {chatbotConversations.map((c) => (
          <li key={c.id} className="border p-2">
            <strong>{c.user_message}</strong> → {c.bot_response}
          </li>
        ))}
      </ul>

      {/* Chatbot Messages */}
      <h2 className="text-xl font-bold mt-5">Chatbot Messages</h2>
      <ul>
        {chatbotMessages.map((msg) => (
          <li key={msg.id} className="border p-2">
            <strong>{msg.user_message}</strong> → {msg.bot_response}
          </li>
        ))}
      </ul>

      {/* Feedback */}
      <h2 className="text-xl font-bold mt-5">User Feedback</h2>
      <ul>
        {feedback.map((f) => (
          <li key={f.id} className="border p-2">
            {f.participant} - {f.feedback_text}
          </li>
        ))}
      </ul>

      {/* Metric Sessions */}
      <h2 className="text-xl font-bold mt-5">Metric Sessions</h2>
      <ul>
        {metricSessions.map((session) => (
          <li key={session.id} className="border p-2">
            {session.participant} - {session.session_date} - {session.metric_score}
          </li>
        ))}
      </ul>

      {/* Participants */}
      <h2 className="text-xl font-bold mt-5">Participants</h2>
      <ul>
        {participants.map((p) => (
          <li key={p.id} className="border p-2">
            {p.name} - {p.age} years old
          </li>
        ))}
      </ul>

      {/* Sports Leadership Evaluations */}
      <h2 className="text-xl font-bold mt-5">Leadership Evaluations</h2>
      <ul>
        {leadershipEvaluations.map((l) => (
          <li key={l.id} className="border p-2">
            {l.participant} - Score: {l.evaluation_score}
          </li>
        ))}
      </ul>

      {/* Notifications */}
      <h2 className="text-xl font-bold mt-5">Notifications</h2>
      <ul>
        {notifications.map((n) => (
          <li key={n.id} className="border p-2">
            {n.message} - {n.timestamp}
          </li>
        ))}
      </ul>

      {/* Additional Chart Component */}
      <Chart />
    </div>
  );
};

export default Dashboard;
