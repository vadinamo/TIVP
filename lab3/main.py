from quadrilateral_worker import QuadrilateralWorker

print(QuadrilateralWorker(2, 2, 2, 2, 90, 90, 90, 90).type)  # Square
print(QuadrilateralWorker(1, 2, 1, 2, 90, 90, 90, 90).type)  # Rectangle
print(QuadrilateralWorker(2, 2, 2, 2, 60, 120, 60, 120).type)  # Rhombus
print(QuadrilateralWorker(1, 2, 1, 2, 60, 120, 60, 120).type)  # Parallelogram
print(QuadrilateralWorker(1, 2, 1, 1, 60, 120, 120, 60).type)  # Trapezoid
print(QuadrilateralWorker(1, 1, 2, 2, 60, 120, 120, 60).type)  # Kite = дельтоид
print(QuadrilateralWorker(1, 2, 3, 4, 60, 120, 120, 60).type)  # Quadrilateral
