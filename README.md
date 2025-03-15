# 🗓️ My SQL Journey: From Fundamentals to Advanced Data Mastery!

[![SQL Portfolio](https://img.shields.io/badge/Portfolio-Data%20Analysis-informational)](https://github.com/TeslimAdeyanju/sql-code-portfolio)

[![Notion](https://img.shields.io/badge/Documentation-Notion-brightgreen)](https://notion.so/https://teslimuthmanadeyanju.notion.site/BASIC-SQL-3e0482d698324d7ca389a41efa3c17d8?pvs=4)

Welcome to my SQL Journey! This repository is a living record of my exploration into SQL and MySQL, showcasing essential skills like column and table aliases, joins, aggregations, and conditional filtering. Each section represents a milestone in my learning path, crafted to deepen my understanding of SQL’s power and versatility in real-world data analysis..

But here’s the exciting part: I’ve integrated Python to bring these SQL queries to life! Using `mysql.connector`, I connect directly to MySQL from Python, and with the help of `pandas`, I transform raw query results into clean, easy-to-read data frames. This combination lets me explore data interactively and visualize results right within my Python scripts—turning each query into a more insightful experience.

## 📂 Portfolio Overview

This portfolio is organized into sections that document my SQL proficiency journey:

- **Querying and Filtering**: Core SQL skills for conditional data extraction.
- **Table Joins and Relationships**: Leveraging relational database principles.
- **Aggregations and Summaries**: Summarizing data for deeper insights.
- **Subqueries and Nested Statements**: Tackling complex data needs efficiently.

Each section serves as a building block, where I’ve combined SQL with Python to transform data into insights.

## Dive Deeper on My Notion Page 📘

For a detailed look, visit my [Notion Page](https://teslimuthmanadeyanju.notion.site/BASIC-SQL-3e0482d698324d7ca389a41efa3c17d8?pvs=4), where I document each skill, reflect on learning milestones, and provide additional resources. This page is your one-stop resource for:

- **In-depth explanations** of SQL concepts and techniques
- **Personal reflections** and learning milestones
- **Additional resources** to deepen your SQL knowledge

This repository and my Notion page together offer a comprehensive view of my SQL journey, connecting learning and real-world application. Let’s uncover insights from SQL, one query at a time!

---

### 1. 🧭 MySQL Basics

This is where my journey began, learning the fundamental SQL operations needed to manage and query data. Understanding the basics of SQL was crucial in building a solid foundation for more complex tasks.

- **[Querying Data](https://github.com/TeslimAdeyanju/1-Portfolio-MySQL-Journey-Fundamentals-to-Advanced-Mastery/blob/main/1-mysql-basics/1.1-select-sql-notebook.ipynb)**: My first SQL statements! Focusing on how to retrieve data from tables using simple `SELECT` queries.
- **[Sorting Data](https://github.com/TeslimAdeyanju/1-Portfolio-MySQL-Journey-Fundamentals-to-Advanced-Mastery/blob/main/1-mysql-basics/1.2-sorting-sql-notebook.ipynb)**: I explored the power of organizing results with `ORDER BY`, a vital tool for any analyst.

---

### 2. 🔍 Filtering Data

Moving forward, I learned how to filter data precisely, allowing me to refine my queries for specific insights. These techniques taught me how to extract just the data I needed from large datasets.

- **[WHERE and DISTINCT](https://github.com/TeslimAdeyanju/1-Portfolio-MySQL-Journey-Fundamentals-to-Advanced-Mastery/blob/main/2-filtering-data/2.1-filtering-data-sql-notebook.ipynb)**: Filtering rows was a game-changer! I learned to apply conditions to hone in on relevant data and eliminate duplicates.


---

### 3. 🌐 Joining Tables

Joining tables felt like unlocking a new dimension in SQL. Here, I learned how to combine data from multiple sources, an essential skill for creating comprehensive data reports. Each type of join has taught me different approaches to merging datasets, allowing me to choose the best method based on the results I need.

- **[INNER JOIN](https://github.com/TeslimAdeyanju/1-Portfolio-MySQL-Journey-Fundamentals-to-Advanced-Mastery/blob/main/3-joining-tables/3.2-inner-join-sql-notebook.ipynb)**: I started with INNER JOINs, which only bring together data when matches exist in both tables. This join type is perfect when I need results that meet strict criteria across two tables.

- **[LEFT JOIN](https://github.com/TeslimAdeyanju/1-Portfolio-MySQL-Journey-Fundamentals-to-Advanced-Mastery/blob/main/3-joining-tables/3.3-left-join-sql-notebook.ipynb)**: LEFT JOIN introduced me to the importance of keeping unmatched data from the left table. When there’s no corresponding data in the right table, it fills the gaps with `NULL`. This join is especially useful when I want all data from the primary table (left table) and any matched data from the secondary table.

- **[RIGHT JOIN](https://github.com/TeslimAdeyanju/1-Portfolio-MySQL-Journey-Fundamentals-to-Advanced-Mastery/blob/main/3-joining-tables/3.4-right-join-sql-notebook.ipynb)**: Learning RIGHT JOIN was the reverse experience of the LEFT JOIN. Here, I keep all data from the right table and match it with the left table where possible. If there’s no match in the left table, SQL fills the missing entries with `NULL`. This approach is valuable when my primary interest is in the complete dataset of the right table while including any relevant data from the left table.

- **[SELF JOIN](https://github.com/TeslimAdeyanju/1-Portfolio-MySQL-Journey-Fundamentals-to-Advanced-Mastery/blob/main/3-joining-tables/3.5-self-join-sql-notebook.ipynb)**: SELF JOIN opened up a unique perspective by allowing me to join a table to itself. This is useful when comparing rows within the same table, such as finding pairs of employees with the same manager or comparing dates within a single dataset. By using table aliases, I could treat the same table as two distinct entities in the query, expanding the scope of analysis I could perform within a single dataset.

Each of these join types gives me control over how I handle matched and unmatched data across tables, allowing me to build robust, comprehensive datasets tailored to specific analytical needs. From precise filtering with INNER JOIN to comparing entries within a single table using SELF JOIN, I’ve learned how to approach complex data relationships with flexibility and depth.

---

### 4. 📂 Aggregations and Grouping

Aggregations were my introduction to data summarization, where I could extract valuable insights from groups within my data. Grouping allowed me to observe trends and analyze data at a higher level.

- **[GROUP BY](https://github.com/TeslimAdeyanju/1-Portfolio-MySQL-Journey-Fundamentals-to-Advanced-Mastery/blob/main/4-grouping-data/4.1-group-by-sql-notebook.ipynb)**: With `GROUP BY`, I began to organize my data into meaningful categories.
- **[HAVING](https://github.com/TeslimAdeyanju/1-Portfolio-MySQL-Journey-Fundamentals-to-Advanced-Mastery/blob/main/4-grouping-data/4.2-group-by-sql-notebook.ipynb)**: Filtering groups with `HAVING` brought in-depth analysis, allowing me to set conditions on aggregated results.

---

### 5. 🧩 Subqueries

Subqueries opened up new ways to approach SQL challenges, letting me nest queries to handle more complex data scenarios. This section highlights how I learned to structure queries within queries.

- **[Simple Subquery](https://github.com/yourusername/sql-code-portfolio/blob/main/05_subqueries_simple.sql)**: My first attempt at subqueries, where I embedded one query inside another.
- **[Derived Table](https://github.com/yourusername/sql-code-portfolio/blob/main/05_subqueries_derived_table.sql)**: Using subqueries as temporary tables helped simplify complex query structures.

---

### 6. 🛠️ Set Operations

Learning set operations like `UNION`, `INTERSECT`, and `EXCEPT` allowed me to combine or compare result sets. These operations expanded my ability to compare datasets and unify results across different queries.

- **[UNION](https://github.com/TeslimAdeyanju/my-SQL-Journey-From-Fundamentals-to-Advanced-Data-Mastery/blob/main/6-Set%20Operations/6.1_union_sql_portfolio_notebook%20copy%202.ipynb)**: `UNION` became a valuable tool for merging datasets without duplicating entries.
- **[INTERSECTION](https://github.com/TeslimAdeyanju/my-SQL-Journey-From-Fundamentals-to-Advanced-Data-Mastery/blob/main/6-Set%20Operations/6.2_intersect_sql_portfolio_notebook%20copy.ipynb)** `INTERSECTION` useful for combinining common columns in two or more tables
- **[EXCEPT](https://github.com/TeslimAdeyanju/my-SQL-Journey-From-Fundamentals-to-Advanced-Data-Mastery/blob/main/6-Set%20Operations/6.3_except_sql_portfolio_notebook.ipynb)** `EXCEPT` commonly use to exclude a columns in a tables.

---

### 7. 🗄️ Database and Table Management

Managing databases and tables helped me gain confidence in SQL as a backend developer's tool. Here, I learned to create and modify databases and tables, a vital skill for managing structured data.

- **[CREATE DATABASE](https://github.com/yourusername/sql-code-portfolio/blob/main/07_database_management_create_database.sql)**: Setting up databases from scratch!
- **[CREATE TABLE](https://github.com/yourusername/sql-code-portfolio/blob/main/07_database_management_create_table.sql)**: Designing table structures taught me the importance of data organization.

---

### 8. 🔐 Constraints and Data Integrity

As I advanced, I learned how to use constraints to enforce data integrity. Constraints ensure that data entries are consistent and reliable, essential for trustworthy databases.

- **[PRIMARY KEY](https://github.com/yourusername/sql-code-portfolio/blob/main/08_constraints_primary_key.sql)**: Defining unique identifiers for each table row.
- **[FOREIGN KEY](https://github.com/yourusername/sql-code-portfolio/blob/main/08_constraints_foreign_key.sql)**: Creating relationships between tables by linking primary keys.

---

## 🎯 Purpose and Applications

This portfolio serves as:

- **Educational Material**: A guide for learning essential SQL techniques, with easy-to-follow examples.
- **Showcase of Expertise**: Evidence of my SQL proficiency, demonstrating real-world skills in data analysis, reporting, and database management.

## 🌐 Further Documentation and Learning Journey

For more in-depth notes and reflections on each topic, visit my [Notion Page](https://notion.so/your-notion-link). This page documents insights, learning milestones, and additional resources, providing a complete picture of my SQL journey.

### 📬 **Get in Touch**

I’m always excited to collaborate on data-driven projects, particularly those involving SQL analytics. Feel free to connect with me!

📧 [info@adeyanjuteslim.co.uk](mailto:info@adeyanjuteslim.co.uk)  
🌍 [adeyanjuteslim.co.uk](https://adeyanjuteslim.co.uk)  
💼 [LinkedIn](https://www.linkedin.com/in/adeyanjuteslimuthman)

---
