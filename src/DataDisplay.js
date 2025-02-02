import React from 'react';

const DataDisplay = ({ data }) => {
  return (
    <ul>
      {data.map((item, index) => (
        <li key={index}>{item.name}</li> // Replace `name` with the field from your API response
      ))}
    </ul>
  );
};

export default DataDisplay;

