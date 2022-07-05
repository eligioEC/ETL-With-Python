import pymysql


class Database:
    def connect(self):

        return pymysql.connect(host="localhost", user="root", password="", database="proyectodae", charset='utf8mb4')

    def readhechos(self,id):
        con = Database.connect(self)
        cursor = con.cursor(pymysql.cursors.DictCursor)

        try:
            if id == None:
                cursor.execute("SELECT * FROM tb_hechos_venta")
            else:
                cursor.execute(
                    "SELECT * FROM tb_hechos_venta where id = %s", (id))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()


    def readproductos(self,id):
        con = Database.connect(self)
        cursor = con.cursor(pymysql.cursors.DictCursor)

        try:
            if id == None:
                cursor.execute("SELECT * FROM tb_productos")
            else:
                cursor.execute(
                    "SELECT * FROM tb_productos where id = %s", (id))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def readclientes(self,id):
        con = Database.connect(self)
        cursor = con.cursor(pymysql.cursors.DictCursor)

        try:
            if id == None:
                cursor.execute("SELECT * FROM tb_clientes")
            else:
                cursor.execute(
                    "SELECT * FROM tb_clientes where id = %s", (id))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def readProductosMasVendidoCategori(self,name_cat):
        con = Database.connect(self)
        cursor = con.cursor(pymysql.cursors.DictCursor)

        try:
            if name_cat == '':
                cursor.execute("SELECT p.category_name, p.product_name, COUNT(1)\
                                FROM `tb_productos` AS p\
                                LEFT JOIN  `tb_hechos_venta` AS h ON  p.product_id = h.order_item_product_id\
                                GROUP BY p.category_name, p.product_name\
                                ORDER BY COUNT(1) DESC")
            else:
                cursor.execute(
                                "SELECT sc.category_name, sc.product_name, MAX(sc.cantidad)\
                                FROM (\
                                    SELECT p.category_name, p.product_name, COUNT(1) AS cantidad\
                                    FROM `tb_productos` AS p\
                                    LEFT JOIN  `tb_hechos_venta` AS h ON  p.product_id = h.order_item_product_id\
                                    GROUP BY p.category_name, p.product_name\
                                    ORDER BY COUNT(1) DESC\
                                ) AS sc\
                                WHERE sc.category_name = %s", (name_cat))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO phone_book(name,phone,address) VALUES(%s, %s, %s)",
                           (data['name'], data['phone'], data['address'],))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def update(self, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE phone_book set name = %s, phone = %s, address = %s where id = %s",
                           (data['name'], data['phone'], data['address'], data["id"],))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def delete(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM phone_book where id = %s", (id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()
