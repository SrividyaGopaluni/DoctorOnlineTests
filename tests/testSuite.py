from unittest import TestLoader, TestSuite, TextTestRunner
from Patient_Login import AAF_Test1
from Staff_Login import AAF_Test2
from patient_register import AAF_Test3
from Staff_register import AAF_Test4
from patient_pricing_list import AAF_Test5
from patient_doctor_details import AAF_Test6
from patient_book_appointment import AAF_Test7
from staff_adddoctor import AAF_Test8
from staff_addpatient import AAF_Test9
from staff_editdoctor import AAF_Test10
from staff_editpatient import AAF_Test11
from staff_view_doctors import AAF_Test12
from staff_view_patients import AAF_Test13
from staff_viewbookings import AAF_Test14


if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(AAF_Test1),
        loader.loadTestsFromTestCase(AAF_Test2),
        loader.loadTestsFromTestCase(AAF_Test3),
        loader.loadTestsFromTestCase(AAF_Test4),
        loader.loadTestsFromTestCase(AAF_Test5),
        loader.loadTestsFromTestCase(AAF_Test6),
        loader.loadTestsFromTestCase(AAF_Test7),
        loader.loadTestsFromTestCase(AAF_Test8),
        loader.loadTestsFromTestCase(AAF_Test9),
        loader.loadTestsFromTestCase(AAF_Test10),
        loader.loadTestsFromTestCase(AAF_Test11),
        loader.loadTestsFromTestCase(AAF_Test12),
        loader.loadTestsFromTestCase(AAF_Test13),
        loader.loadTestsFromTestCase(AAF_Test14),



    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)