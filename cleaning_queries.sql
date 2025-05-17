SELECT CustomerID , COUNT(*) AS cnt
FROM `customer_churn_dataset-testing-master`
GROUP BY CustomerID
HAVING cnt > 1;

WITH ranked AS (
  select*, ROW_NUMBER() OVER (PARTITION BY CustomerID ORDER BY CustomerID) AS rn
  FROM `customer_churn_dataset-testing-master`
)
delete FROM `customer_churn_dataset-testing-master`
WHERE CustomerID IN (
  SELECT CustomerID FROM ranked WHERE rn > 1
);

SELECT * 
FROM `customer_churn_dataset-testing-master`
 WHERE `Total Spend` = '' OR `Total Spend` IS NULL;
 
 UPDATE `customer_churn_dataset-testing-master` 
 SET TotalCharges = NULL 
 WHERE TRIM(TotalCharges) = '';


ALTER TABLE  `customer_churn_dataset-testing-master` 
MODIFY TotalCharges DECIMAL(10,2);

UPDATE `customer_churn_dataset-testing-master` 
SET customerID = TRIM(customerID);

COMMIT;

select*
from `customer_churn_dataset-testing-master`; 


