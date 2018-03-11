require './dorothy/dorothy'

Lita.configure do |config|
  config.http.port = 6335
  config.robot.adapter = :shell
  config.robot.name = 'Dorothy'
  config.robot.mention_name = 'dorothy'
end
