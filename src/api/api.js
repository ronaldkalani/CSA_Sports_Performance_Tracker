import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000/api"; // Update this with your backend URL

// Create a reusable Axios instance
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// API Calls for Different Models
export const fetchAssessmentMetrics = () => api.get("/assessment-metrics/");
export const fetchAthleteGoals = () => api.get("/athlete-goals/");
export const fetchChatbotConversations = () => api.get("/chatbot-conversations/");
export const sendChatbotMessage = (message) => api.post("/chatbot-conversations/", { message });
export const fetchChatbotMessages = () => api.get("/chatbot-messages/");
export const fetchFeedback = () => api.get("/feedback/");
export const fetchMetrics = () => api.get("/metrics/");
export const fetchMetricSessions = () => api.get("/metric-sessions/");
export const fetchNotifications = () => api.get("/notifications/");
export const fetchParticipants = () => api.get("/participants/");
export const fetchSportsLeadershipEvaluations = () => api.get("/sports-leadership/");

export default api;

