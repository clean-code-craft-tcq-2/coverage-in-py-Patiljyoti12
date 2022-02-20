import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_low_limit(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    
  def test_infers_breach_as_per_high_limit(self):
    self.assertTrue(typewise_alert.infer_breach(120, 50,100) == 'TOO_HIGH')

  def test_infers_breach_as_per_normal_limit(self):
    self.assertTrue(typewise_alert.infer_breach(60, 50, 100) == 'NORMAL')
    
  def test_send_to_controller_low_breachType(self):
    self.assertTrue(typewise_alert.send_to_controller('TOO_LOW') == f'{0xfeed}, TOO_LOW')

  def test_send_to_controller_high_breachType(self):
    self.assertTrue(typewise_alert.send_to_controller('TOO_HIGH') == f'{0xfeed}, TOO_HIGH')

  def test_send_to_email_for_low_breach_type(self):
    self.assertTrue(typewise_alert.send_to_email('TOO_LOW') ==f'To: a.b@c.com,Hi, the temperature is too low' )

  def test_send_to_email_for_high_breach_type(self):
        self.assertTrue(typewise_alert.send_to_email('TOO_HIGH') ==f'To: a.b@c.com,Hi, the temperature is too high' )
   
  def test_classify_temperature_breach_with_passive_cooling_type(self):
    self.assertTrue(typewise_alert.classify_temperature_breach(20,'PASSIVE')=='NORMAL')
    self.assertTrue(typewise_alert.classify_temperature_breach(-10,'PASSIVE')=='TOO_LOW')
    self.assertTrue(typewise_alert.classify_temperature_breach(120,'PASSIVE')=='TOO_HIGH')
    
  def test_classify_temperature_breach_with_high_active_cooling_type(self):
    self.assertTrue(typewise_alert.classify_temperature_breach(30,'HI_ACTIVE')=='NORMAL')
    self.assertTrue(typewise_alert.classify_temperature_breach(-10,'HI_ACTIVE')=='TOO_LOW')
    self.assertTrue(typewise_alert.classify_temperature_breach(120,'HI_ACTIVE')=='TOO_HIGH')

  def test_classify_temperature_breach_with_medium_cooling_type(self):
    self.assertTrue(typewise_alert.classify_temperature_breach(20,'MED_ACTIVE')=='NORMAL')
    self.assertTrue(typewise_alert.classify_temperature_breach(-10,'MED_ACTIVE')=='TOO_LOW')
    self.assertTrue(typewise_alert.classify_temperature_breach(120,'MED_ACTIVE')=='TOO_HIGH')
    
    
    
if __name__ == '__main__':
  unittest.main()
