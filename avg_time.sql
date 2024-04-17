-- average "dwell" time per page
SELECT
    current_url,
    AVG(session_duration) AS average_dwell_time
FROM
    fact
GROUP BY
    current_url
ORDER BY
    average_dwell_time DESC;