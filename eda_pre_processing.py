import pandas as pd

class EDA:

    def datetime(df,col_name):
        df[col_name]=pd.to_datetime(df[col_name])
        return df
    
    def categoricalByValue(df,value):
        object_cols = df.select_dtypes(include=['object'])
        for i in object_cols:
            if value>=df[i].value_counts().nunique():
                df[i]=df[i].astype('category')
        return df
    
    
    def categoricalByName(df,cols_name):
        for i in cols_name:
            df[i] = df[i].astype('category')
        return df
    
    
    def cleanNaNCol(df,percent=50):
        def listToDrop(df,percent):
            drop_list = []
            column_NA=[]
            column_total_record = df.shape[0]
            for i in df.columns:
                val = round(df[i].isna().sum()/column_total_record*100,2)
                column_NA.append(val)
            for i,j in enumerate(column_NA):
                if j>=percent:
                     drop_list.append(df.columns[i])        
            return drop_list

        def drop(df,percent):
            list_ = listToDrop(df,percent)
            df.drop(list_,axis=1,inplace=True)
            return df

        return drop(df,percent)
    

    def fillna(df,m=1):
        if m==1:
            df.fillna(df.mean(),inplace=True)
        elif m==2:
            df.fillna(df.median(),inplace=True)
        return df
    
    
#     def fillna(df,m=1):
#         numeric_cols = df.select_dtypes(include=['int64','float64']).columns
#         if m==1:
#             df[numeric_cols].fillna(df.mean(),inplace=True)
#         elif m==2:
#             df[numeric_cols].fillna(df.median(),inplace=True)
#         return df
