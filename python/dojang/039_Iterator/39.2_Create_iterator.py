# source activate py36gputorch041
# cd /mnt/1T-5e7/mycodehtml/p_lang/python/dojang
# rm e.l && python 39.2_이터레이터_만들기.py 2>&1 | tee -a e.l && code e.l


# Create iterator class
# class Iterator_name_you_want:
#   def __iter__(self):
#     Code

#   def __next__(self):
#     Code

# ================================================================================
class Counter:
  def __init__(self,stop):
    self.current=0
    self.stop=stop

  def __iter__(self):
    return self

  def __next__(self):
    if self.current<self.stop:
      r=self.current
      self.current+=1
      return r
    else:
      raise StopIteration

for i in Counter(3):
  print(i,end=' ')

# ================================================================================
# Unpacking iterator

a,b,c=Counter(3)
a,b,c,d,e=Counter(5)
a,_,c,d=range(4)

# ================================================================================
