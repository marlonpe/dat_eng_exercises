-- most visited pages
SELECT
    current_url,
    COUNT(*) AS visit_count
FROM
    fact
GROUP BY
    current_url
ORDER BY
    visit_count DESC
LIMIT 10;