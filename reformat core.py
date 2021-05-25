import pandas as pd

def reformat():

    df = pd.read_excel("manifest.xlsx")
    df = df.drop(['Outbound Time'],axis=1)
    prim = list(df.columns)[ : 33]
    df.set_index(prim,inplace=True)

    df[['Declared Name 1','Product Name 1','Declared Value 1','Declared QTY 1']].rename(columns={'Declared Name 1': 'Category','Product Name 1' : 'Content','Declared Value 1':'Unit Price','Declared QTY 1':'QTY'})

    target = pd.concat([df[['Declared Name 1','Product Name 1','Declared Value 1','Declared QTY 1']].rename(columns={'Declared Name 1': 'Category','Product Name 1' : 'Content','Declared Value 1':'Unit Price','Declared QTY 1':'QTY'}),
                    df[['Declared Name 2','Product Name 2','Declared Value 2','Declared QTY 2']].rename(columns={'Declared Name 2': 'Category','Product Name 2' : 'Content','Declared Value 2':'Unit Price','Declared QTY 2':'QTY'}),
                    df[['Declared Name 3','Product Name 3','Declared Value 3','Declared QTY 3']].rename(columns={'Declared Name 3': 'Category','Product Name 3' : 'Content','Declared Value 3':'Unit Price','Declared QTY 3':'QTY'}),
                    df[['Declared Name 4','Product Name 4','Declared Value 4','Declared QTY 4']].rename(columns={'Declared Name 4': 'Category','Product Name 4' : 'Content','Declared Value 4':'Unit Price','Declared QTY 4':'QTY'}),
                    df[['Declared Name 5','Product Name 5','Declared Value 5','Declared QTY 5']].rename(columns={'Declared Name 5': 'Category','Product Name 5' : 'Content','Declared Value 5':'Unit Price','Declared QTY 5':'QTY'}),
                    df[['Declared Name 6','Product Name 6','Declared Value 6','Declared QTY 6']].rename(columns={'Declared Name 6': 'Category','Product Name 6' : 'Content','Declared Value 6':'Unit Price','Declared QTY 6':'QTY'}),
                    df[['Declared Name 7','Product Name 7','Declared Value 7','Declared QTY 7']].rename(columns={'Declared Name 7': 'Category','Product Name 7' : 'Content','Declared Value 7':'Unit Price','Declared QTY 7':'QTY'}),
                    df[['Declared Name 8','Product Name 8','Declared Value 8','Declared QTY 8']].rename(columns={'Declared Name 8': 'Category','Product Name 8' : 'Content','Declared Value 8':'Unit Price','Declared QTY 8':'QTY'}),
                    df[['Declared Name 9','Product Name 9','Declared Value 9','Declared QTY 9']].rename(columns={'Declared Name 9': 'Category','Product Name 9' : 'Content','Declared Value 9':'Unit Price','Declared QTY 9':'QTY'}),
                    df[['Declared Name 10','Product Name 10','Declared Value 10','Declared QTY 10']].rename(columns={'Declared Name 10': 'Category','Product Name 10' : 'Content','Declared Value 10':'Unit Price','Declared QTY 10':'QTY'}),
                    df[['Declared Name 11','Product Name 11','Declared Value 11','Declared QTY 11']].rename(columns={'Declared Name 11': 'Category','Product Name 11' : 'Content','Declared Value 11':'Unit Price','Declared QTY 11':'QTY'}),
                    df[['Declared Name 12','Product Name 12','Declared Value 12','Declared QTY 12']].rename(columns={'Declared Name 12': 'Category','Product Name 12' : 'Content','Declared Value 12':'Unit Price','Declared QTY 12':'QTY'}),
                    df[['Declared Name 13','Product Name 13','Declared Value 13','Declared QTY 13']].rename(columns={'Declared Name 13': 'Category','Product Name 13' : 'Content','Declared Value 13':'Unit Price','Declared QTY 13':'QTY'}),
                    df[['Declared Name 14','Product Name 14','Declared Value 14','Declared QTY 14']].rename(columns={'Declared Name 14': 'Category','Product Name 14' : 'Content','Declared Value 14':'Unit Price','Declared QTY 14':'QTY'}),
                    df[['Declared Name 15','Product Name 15','Declared Value 15','Declared QTY 15']].rename(columns={'Declared Name 15': 'Category','Product Name 15' : 'Content','Declared Value 15':'Unit Price','Declared QTY 15':'QTY'}),
                    df[['Declared Name 16','Product Name 16','Declared Value 16','Declared QTY 16']].rename(columns={'Declared Name 16': 'Category','Product Name 16' : 'Content','Declared Value 16':'Unit Price','Declared QTY 16':'QTY'}),
                    df[['Declared Name 17','Product Name 17','Declared Value 17','Declared QTY 17']].rename(columns={'Declared Name 17': 'Category','Product Name 17' : 'Content','Declared Value 17':'Unit Price','Declared QTY 17':'QTY'}),
                    df[['Declared Name 18','Product Name 18','Declared Value 18','Declared QTY 18']].rename(columns={'Declared Name 18': 'Category','Product Name 18' : 'Content','Declared Value 18':'Unit Price','Declared QTY 18':'QTY'}),
                    df[['Declared Name 19','Product Name 19','Declared Value 19','Declared QTY 19']].rename(columns={'Declared Name 19': 'Category','Product Name 19' : 'Content','Declared Value 19':'Unit Price','Declared QTY 19':'QTY'}),
                    df[['Declared Name 20','Product Name 20','Declared Value 20','Declared QTY 20']].rename(columns={'Declared Name 20': 'Category','Product Name 20' : 'Content','Declared Value 20':'Unit Price','Declared QTY 20':'QTY'}),
                    df[['Declared Name 21','Product Name 21','Declared Value 21','Declared QTY 21']].rename(columns={'Declared Name 21': 'Category','Product Name 21' : 'Content','Declared Value 21':'Unit Price','Declared QTY 21':'QTY'}),
                    df[['Declared Name 22','Product Name 22','Declared Value 22','Declared QTY 22']].rename(columns={'Declared Name 22': 'Category','Product Name 22' : 'Content','Declared Value 22':'Unit Price','Declared QTY 22':'QTY'}),
                    df[['Declared Name 23','Product Name 23','Declared Value 23','Declared QTY 23']].rename(columns={'Declared Name 23': 'Category','Product Name 23' : 'Content','Declared Value 23':'Unit Price','Declared QTY 23':'QTY'}),
                    df[['Declared Name 24','Product Name 24','Declared Value 24','Declared QTY 24']].rename(columns={'Declared Name 24': 'Category','Product Name 24' : 'Content','Declared Value 24':'Unit Price','Declared QTY 24':'QTY'}),
                    df[['Declared Name 25','Product Name 25','Declared Value 25','Declared QTY 25']].rename(columns={'Declared Name 25': 'Category','Product Name 25' : 'Content','Declared Value 25':'Unit Price','Declared QTY 25':'QTY'}),
                    df[['Declared Name 26','Product Name 26','Declared Value 26','Declared QTY 26']].rename(columns={'Declared Name 26': 'Category','Product Name 26' : 'Content','Declared Value 26':'Unit Price','Declared QTY 26':'QTY'}),
                    df[['Declared Name 27','Product Name 27','Declared Value 27','Declared QTY 27']].rename(columns={'Declared Name 27': 'Category','Product Name 27' : 'Content','Declared Value 27':'Unit Price','Declared QTY 27':'QTY'}),
                    df[['Declared Name 28','Product Name 28','Declared Value 28','Declared QTY 28']].rename(columns={'Declared Name 28': 'Category','Product Name 28' : 'Content','Declared Value 28':'Unit Price','Declared QTY 28':'QTY'}),
                    df[['Declared Name 29','Product Name 29','Declared Value 29','Declared QTY 29']].rename(columns={'Declared Name 29': 'Category','Product Name 29' : 'Content','Declared Value 29':'Unit Price','Declared QTY 29':'QTY'}),
                    df[['Declared Name 30','Product Name 30','Declared Value 30','Declared QTY 30']].rename(columns={'Declared Name 30': 'Category','Product Name 30' : 'Content','Declared Value 30':'Unit Price','Declared QTY 30':'QTY'}),
                    df[['Declared Name 31','Product Name 31','Declared Value 31','Declared QTY 31']].rename(columns={'Declared Name 31': 'Category','Product Name 31' : 'Content','Declared Value 31':'Unit Price','Declared QTY 31':'QTY'}),
                    df[['Declared Name 32','Product Name 32','Declared Value 32','Declared QTY 32']].rename(columns={'Declared Name 32': 'Category','Product Name 32' : 'Content','Declared Value 32':'Unit Price','Declared QTY 32':'QTY'}),
                    df[['Declared Name 33','Product Name 33','Declared Value 33','Declared QTY 33']].rename(columns={'Declared Name 33': 'Category','Product Name 33' : 'Content','Declared Value 33':'Unit Price','Declared QTY 33':'QTY'}),
                    df[['Declared Name 34','Product Name 34','Declared Value 34','Declared QTY 34']].rename(columns={'Declared Name 34': 'Category','Product Name 34' : 'Content','Declared Value 34':'Unit Price','Declared QTY 34':'QTY'}),
                    df[['Declared Name 35','Product Name 35','Declared Value 35','Declared QTY 35']].rename(columns={'Declared Name 35': 'Category','Product Name 35' : 'Content','Declared Value 35':'Unit Price','Declared QTY 35':'QTY'}),
                    df[['Declared Name 36','Product Name 36','Declared Value 36','Declared QTY 36']].rename(columns={'Declared Name 36': 'Category','Product Name 36' : 'Content','Declared Value 36':'Unit Price','Declared QTY 36':'QTY'}),
                    df[['Declared Name 37','Product Name 37','Declared Value 37','Declared QTY 37']].rename(columns={'Declared Name 37': 'Category','Product Name 37' : 'Content','Declared Value 37':'Unit Price','Declared QTY 37':'QTY'}),
                    df[['Declared Name 38','Product Name 38','Declared Value 38','Declared QTY 38']].rename(columns={'Declared Name 38': 'Category','Product Name 38' : 'Content','Declared Value 38':'Unit Price','Declared QTY 38':'QTY'}),
                    df[['Declared Name 39','Product Name 39','Declared Value 39','Declared QTY 39']].rename(columns={'Declared Name 39': 'Category','Product Name 39' : 'Content','Declared Value 39':'Unit Price','Declared QTY 39':'QTY'}),
                    df[['Declared Name 40','Product Name 40','Declared Value 40','Declared QTY 40']].rename(columns={'Declared Name 40': 'Category','Product Name 40' : 'Content','Declared Value 40':'Unit Price','Declared QTY 40':'QTY'})], join="inner")

    target = target.sort_values(['Category']).reset_index()
    target = pd.DataFrame(target)
    suc = target[~pd.isnull(target['Category'])]
    suc = suc.sort_values(['LM Tracking'])
    postcode = '000000'
    suc['postcode'] = postcode
    total = suc['Unit Price']*suc['QTY']
    suc['Total Value'] = total

    MAWB = input("Please enter MAWB: ")
    suc['MAWB'] = MAWB

    Currency = 'THB'
    suc['Currency'] = Currency

    shitype = 'parcel'
    suc['Shipment Type'] = shitype

    Origin = 'IDN'
    suc['Origin'] = Origin

    Destination = 'BKK'
    suc['Destination'] = Destination

    Creation = '2021-05-16 17:00:13'
    suc['Creation'] = Creation
    suc['Processing'] = Creation

    Package = ''
    suc['Package'] = Package

    COD = 0
    suc['COD'] = COD

    Payment = '0'
    suc['Payment'] = Payment

    HSCODE = ''
    suc['HSCODE'] = HSCODE

    shipcountry = 'Indonesia'
    suc['shipcountry'] = shipcountry

    suc['Postal Code'] = suc['Postal Code'].apply(str)

    count = suc.groupby('LM Tracking').size().reset_index(name='count')
    count.loc[(count['count']>1),'count'] = 'YES'
    count.loc[(count['count']==1),'count'] = 'NO'

    suc = pd.merge(suc,count,on='LM Tracking',how='inner')

    sortcolumn = ['MAWB','LM Tracking','Sender Name','Sender Name','Sender Telephone','Sender Address','shipcountry','postcode','Receiver Name','Receiver Name','Receiver Telephone','Receiver Address','Country','Postal Code','Currency','Content','QTY','Unit Price','Total Value','count','Shipment Type','Parcel Volume','Parcel Weight(KG)','Origin','Destination','Creation','Processing','HSCODE','Category','Carton No','Package','Payment','COD']
    final=suc.reindex(columns=sortcolumn)

    final.to_excel("reformatting sun indonesia.xlsx",index=False)
