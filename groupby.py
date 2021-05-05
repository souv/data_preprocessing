#groupby
test = sales.groupby(by=['region'])

#find specific group
test.get_group("east")

#aggregate in groupby 
test_agg = sales.groupby(by=['region'].aggregate({sales2016:"sum"})
                         
#to make the groupby object into dataframe                         
res = test_agg.reset_index()

#when you plot you input raw data not groupby data                         
res_wide = res.melt(id_vars="region")
sns.barplot(x="region",y="value",data=res_wide,hue="variable")
plt.show()
