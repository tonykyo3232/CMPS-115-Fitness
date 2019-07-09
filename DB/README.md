# How to set up DB schema

Below command will generate `fitness` database and tables described in `EER.png`.  
It's assuming that you have installed mysql and you use bash-like shell.  

```bash
# if your mysql user requires password
mysql -u username -p < schema_generate.sql

# if your mysql user does not require password
#mysql -u username < schema_generate.sql
```
