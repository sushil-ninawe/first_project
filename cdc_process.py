WITH entitlement_changes AS (
    SELECT
        empid,
        enttl_type,
        enttl_value,
        date_provision AS date_start,
        LEAD(date_provision, 1) OVER (PARTITION BY empid, enttl_type ORDER BY date_provision) AS next_date_provision
    FROM
        entitlements
)
SELECT
    empid,
    enttl_type,
    enttl_value,
    date_start,
    CASE
        WHEN next_date_provision IS NOT NULL THEN DATE_SUB(next_date_provision, 1)
        ELSE NULL
    END AS date_end
FROM
    entitlement_changes
ORDER BY
    empid, enttl_type, date_start;
