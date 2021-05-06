import struct

def dat_Open( filename):
  fp = open(filename,'w')
  return( fp)

def dat_OpenB( filename):
  fp = open(filename,'wb')
  return( fp)

def dat_OpenReadB( filename):
  fp = open(filename,'rb')
  return( fp)
  

def dat_Close(fp):
  fp.close()
def dat_CloseB(fp):
  fp.close()


def dat_Save(fp,time,cnt_RL,cnt_RR,speed_RL,speed_RR,current_RL,current_RR,soc_Bat,vol_Bat,pos_localX,pos_localY):
  dataline = str(pos_localY)+'\t'+str(speed_RR)+'\t' \
            +str(vol_Bat)
  fp.write(dataline)

def dat_SaveB(fp,time,cnt_RL,cnt_RR,speed_RL,speed_RR,current_RL,current_RR,soc_Bat,vol_Bat,pos_localX,pos_localY):
  fp.write(struct.pack('f', time))
  fp.write(struct.pack('f', cnt_RL))
  fp.write(b'0xd')

def dat_ReadB(fp):
    data=fp.read(4)
    print(type(data))
    print(type(struct.unpack('f',data)))
    numbers=struct.unpack('f',data)[0]
    print(numbers)
    print(struct.unpack('f',data))
    data=fp.read(4)
    print(struct.unpack('f',data))


fp = dat_OpenB('dat.dat')
dat_SaveB(fp,0.1,102.,10,10,10, 10,10, 100,50.0, 100.0 ,100.001)
dat_CloseB(fp) 

fp = dat_OpenReadB('dat.dat')
dat_ReadB(fp)
dat_CloseB(fp) 