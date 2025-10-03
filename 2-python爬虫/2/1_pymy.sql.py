"""
    使用pymysql模块在mytab表中插入一条表记录
"""
import pymysql

try:
    # 1. 创建数据库连接
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        database='mydb',
        charset='utf8mb4',
        port=3306
    )

    print("✅ 数据库连接成功！")

    # 2. 创建游标对象
    cursor = db.cursor()

    # 3. 插入数据
    # 修正：明确指定列名，避免值顺序错误
    ins = 'INSERT INTO mytab (title, director, release_date) VALUES (%s, %s, %s)'

    # 修正：li 应该是元组，不是列表包含元组
    li = ('大话西游', '周星驰', '1994-01-01')

    # 修正：使用 cursor 而不是 cur
    cursor.execute(ins, li)

    # 4. 提交到数据库执行
    db.commit()
    print("✅ 数据插入成功！")

    # 5. 验证插入结果
    cursor.execute("SELECT * FROM mytab")
    results = cursor.fetchall()
    print("📊 当前表中的数据:")
    for row in results:
        print(row)

    # 6. 关闭游标和连接
    cursor.close()
    db.close()
    print("✅ 连接已关闭")

except pymysql.Error as e:
    print(f"❌ 数据库错误: {e}")
    # 发生错误时回滚
    if 'db' in locals():
        db.rollback()
except Exception as e:
    print(f"❌ 其他错误: {e}")

