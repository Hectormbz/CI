import unittest
import os
import pandas as pd
import numpy as np
from Functions import increment
class TestFunction(unittest.TestCase):
    
    def test_Increment(self):
        self.assertEqual(increment(5), 6)
        self.assertEqual(increment(-8), -7)
        self.assertEqual(increment(0), 1)
    
    def test_FileSaved(self):
        self.assertTrue(os.path.exists("PipelineData.csv"))

    def test_GraphSaved(self):
        self.assertTrue(os.path.exists("DataPipelinePlot.png"))

    def test_ForNonNumericValues(self):
        df = pd.read_csv("PipelineData.csv")
        self.assertTrue(np.issubdtype(df["x"].dtype, np.number))
        self.assertTrue(np.issubdtype(df["y"].dtype, np.number))

    def test_SlopeandInterceptClose(self):
        df = pd.read_csv("PipelineData.csv")
        x = df["x"].values
        y = df["y"].values
        mFit, bFit = np.polyfit(x, y, 1)
        self.assertAlmostEqual(mFit, 2, delta = 0.3)
        self.assertAlmostEqual(bFit, 5, delta = 0.3)


if __name__ == '__main__':
    unittest.main()