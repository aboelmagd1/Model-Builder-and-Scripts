import arcpy , qrcode
QrCode = r"path\pont_QR"

pathP1 = "https://www.google.com/maps/search/?api=1&query="
pathP2 = ""
fullPath = ""

with arcpy.da.SearchCursor(QrCode , ["SHAPE@" , "LP_ID"] ) as cur :
        for i,r in enumerate(cur) :
            point = r[0]
            x , y = point.centroid.X , point.centroid.Y
            pathP2 = f"{y},{x}"
            fullPath = f"{pathP1}{pathP2}"
            print(fullPath)
            name = r[1]
            img = qrcode.make(fullPath)
            img.save("img{0}.png".format(name))