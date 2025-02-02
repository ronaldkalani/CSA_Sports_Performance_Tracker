import React, { useEffect, useState } from 'react';
import { getAssessmentMetrics } from '../api';

const AssessmentMetrics = () => {
    const [metrics, setMetrics] = useState([]);

    useEffect(() => {
        getAssessmentMetrics().then(data => {
            if (data) setMetrics(data);
        });
    }, []);

    return (
        <div>
            <h2>Assessment Metrics</h2>
            <ul>
                {metrics.map(metric => (
                    <li key={metric.id}>{metric.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default AssessmentMetrics;
