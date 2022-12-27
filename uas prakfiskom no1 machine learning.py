from sklearn.neighbors import NearestCentroid

# Database: Gerbang logika AND
# X = Data, Y = Target
x = [[1,10], [1,20], [1,30], [1,40], [1,50],
     [1,60], [1,70], [1,80], [1,90], [1,100]]
y = [1.8025164595168974, 1.7016102218370153, 1.5487251240825133,
     1.4185405192770202, 1.3661491478700607, 1.4025984150439217,
     1.5095498772983318, 1.6621890164025628, 1.8408476819173034,
     2.033069955971175]
# Training and Classify
clf = NearCentroid()
clf = clf.fit(x,y)

# Prediksi
print ("Logika AND Metode K. Nearest Neighbors (KNN)")
print("Logika = Prediksi")
print ("1 10 = ", clf.predict([[1,10]]))
print ("1 20 = ", clf.predict([[1,20]]))
print ("1 30 = ", clf.predict([[1,30]]))
print ("1 40 = ", clf.predict([[1,40]]))
print ("1 50 = ", clf.predict([[1,50]]))
print ("1 60 = ", clf.predict([[1,60]]))
print ("1 70 = ", clf.predict([[1,70]]))
print ("1 80 = ", clf.predict([[1,80]]))
print ("1 90 = ", clf.predict([[1,90]]))
print ("1 100 = ", clf.predict([[1,100]]))
