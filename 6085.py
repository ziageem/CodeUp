w,h,b=input().split()
w,h,b=int(w),int(h),int(b)
storage=w*h*b/8/1024/1024
print('%.2f'%storage,"MB")