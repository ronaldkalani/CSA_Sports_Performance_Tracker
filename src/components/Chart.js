import React from "react";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from "recharts";

const data = [
  { name: "Jan", performance: 80 },
  { name: "Feb", performance: 90 },
  { name: "Mar", performance: 85 },
];

const Chart = () => {
  return (
    <LineChart width={400} height={300} data={data}>
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="name" />
      <YAxis />
      <Tooltip />
      <Legend />
      <Line type="monotone" dataKey="performance" stroke="#8884d8" />
    </LineChart>
  );
};

export default Chart;
