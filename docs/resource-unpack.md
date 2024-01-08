ABC.mkf unpack examples:

step 1: demkf.py resource/ABC.MKF -p yj1 output files: 0.yj1-154.yj1
step 2: deyj1.py 1.yj1 -o yj1_1.out output files: yj1_1.out
step 3: desmkf.py yj1_1.out -p smkf output files: yj1_1.out.smkf
step 4: derle.py yj1_1.out.smkf -o yj1_1.out.smkf.bmp -p PAT.MKF output files: yj1_1.out.smkf.bmp