import axios from "axios";

// Use environment variable for API URL (fallback to local development)
const API_BASE_URL = process.env.REACT_APP_API_URL || "http://127.0.0.1:8000/api";

// Create a reusable Axios instance
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// Axios Interceptor for handling errors globally (optional)
api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error("API Error:", error.response?.data || error.message);
    return Promise.reject(error);
  }
);

// Generic API Fetcher for GET requests
export const fetchData = async (endpoint) => {
  try {
    const response = await api.get(endpoint);
    return response.data;
  } catch (error) {
    console.error("API fetch error:", error);
    return { error: "Failed to fetch data" };
  }
};

// Specific API Calls
export const fetchAssessmentMetrics = () => fetchData("/assessment-metrics/");
export const fetchAthleteGoals = () => fetchData("/athlete-goals/");
export const fetchChatbotConversations = () => fetchData("/chatbot-conversations/");
export const sendChatbotMessage = (message) => api.post("/chatbot-conversations/", { message });
export const fetchChatbotMessages = () => fetchData("/chatbot-messages/");
export const fetchFeedback = () => fetchData("/feedback/");
export const fetchMetrics = () => fetchData("/metrics/");
export const fetchMetricSessions = () => fetchData("/metric-sessions/");
export const fetchNotifications = () => fetchData("/notifications/");
export const fetchParticipants = () => fetchData("/participants/");
export const fetchSportsLeadershipEvaluations = () => fetchData("/sports-leadership/");

export default api;


