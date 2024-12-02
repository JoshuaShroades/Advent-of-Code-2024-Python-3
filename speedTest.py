import time
# import Day01.part1 as A01
# import Day01.part2 as B01
import Day02.part1 as A02
import Day02.part2 as B02
# import Day03.part1 as A03
# import Day03.part2 as B03
# import Day04.part1 as A04
# import Day04.part2 as B04
# import Day05.part1 as A05
# import Day05.part2 as B05
# import Day06.part1 as A06
# import Day06.part2 as B06
# import Day07.part1 as A07
# import Day07.part2 as B07
# import Day08.part1 as A08
# import Day08.part2 as B08
# import Day09.part1 as A09
# import Day09.part2 as B09
# import Day10.part1 as A10
# import Day10.part2 as B10
# import Day11.part1 as A11
# import Day11.part2 as B11
# import Day12.part1 as A12
# import Day12.part2 as B12

def speedTest(func):
	times = []
	for _ in range(100):
		startTime = time.time()

		value = func.main()

		times.append(time.time() - startTime)

	print("\n" + func.__name__ + ": " + str(value))
	print("Average time (ms): " + str(round(sum(times) / len(times) * 1000, 2)))

# speedTest(A01)
# speedTest(B01)
speedTest(A02)
speedTest(B02)
# speedTest(A03)
# speedTest(B03)
# speedTest(A04)
# speedTest(B04)
# speedTest(A05)
# speedTest(B05)
# speedTest(A06)
# speedTest(B06)
# speedTest(A07)
# speedTest(B07)
# speedTest(A08)
# speedTest(B08)
# speedTest(A09)
# speedTest(B09)
# speedTest(A10)
# speedTest(B10)
# speedTest(A11)
# speedTest(B11)
# speedTest(A12)
# speedTest(B12)
