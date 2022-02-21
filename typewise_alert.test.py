import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    
  def test_send_to_controller_breachType(self):
    self.assertTrue(typewise_alert.send_to_controller('TOO_LOW') == f'{0xfeed}, TOO_LOW')

  def test_send_to_email_for_breach_type(self):
    self.assertTrue(typewise_alert.send_to_email('TOO_HIGH') ==f'To: a.b@c.com,Hi, the temperature is too high' )
   
  def test_classify_temperature_breach_with_passive_cooling_type(self):
    self.assertTrue(typewise_alert.classify_temperature_breach(20,'PASSIVE')=='NORMAL')
    
  def test_classify_temperature_breach_with_high_active_cooling_type(self):
    self.assertTrue(typewise_alert.classify_temperature_breach(-10,'HI_ACTIVE')=='TOO_LOW')
    
  def test_classify_temperature_breach_with_medium_cooling_type(self):
    self.assertTrue(typewise_alert.classify_temperature_breach(120,'MED_ACTIVE')=='TOO_HIGH')
    
  def test_check_and_alert_to_controller(self):
    self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER',-19,"PASSIVE") == f'{0xfeed}, TOO_LOW')
    
  def test_check_and_alert_trigger_email_notification(self):
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL',-10,"PASSIVE") == f'To: a.b@c.com,Hi, the temperature is too low' )
    
    
    
    
    
if __name__ == '__main__':
  unittest.main()
