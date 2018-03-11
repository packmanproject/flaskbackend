from flask import abort, request, make_response, jsonify, json, Response
from flask.json import JSONEncoder
from flask.ext.mysql import MySQL
from config import *

import sys, os

mysql = MySQL()

mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

@app.route('/api/kepegawaian', methods=['GET','POST'])
def get():
    cur = mysql.connect().cursor()
    cur.execute('''select * from biodata_pegawai''')
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify({'data_kepegawaian' : r})


@app.route('/api/kepegawaian/<nip>',methods=['GET','POST'])
def nama(nip):
    cur = mysql.connect().cursor()
    cur.execute("select * from biodata_pegawai WHERE nip=%s",(nip))
    r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify({'data_kepegawaian' : r})


@app.route('/api/kepegawaian/detail', methods=['GET','POST'])
def get_detail():
    cur = mysql.connect().cursor()
    cur.execute('''
        SELECT  * from biodata_pegawai join pekerjaan_pegawai
        on biodata_pegawai.nip=pekerjaan_pegawai.nip
        join pendidikan_pegawai on biodata_pegawai.nip=pendidikan_pegawai.nip 
        join penelitian_pegawai on 
        biodata_pegawai.nip=penelitian_pegawai.nip''')


    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify({'data_kepegawaian' : r})


@app.route('/api/kepegawaian/detail/<nip>',methods=['GET','POST'])
def nama_detail(nip):
    cur = mysql.connect().cursor()
    cur.execute('''SELECT  *
        from biodata_pegawai inner join pekerjaan_pegawai on 
        biodata_pegawai.nip=pekerjaan_pegawai.nip  
        inner join penelitian_pegawai on 
        biodata_pegawai.nip=penelitian_pegawai.nip
        WHERE biodata_pegawai.nip=%s''',(nip))
    #r=cur.fetchall()
    #rv = cur.fetch_row()
    field_name = [field[0] for field in cur.description]
    values = cur.fetchone()
    row = dict(zip(field_name, values))
    
    return jsonify({'data_kepegawaian' : row})


if __name__ == '__main__':
	app.run(debug=True)



