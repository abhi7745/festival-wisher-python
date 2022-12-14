from datetime import date, datetime

# print(date.today())
current_year = date.today()
# print(current_year.year)

import smtplib
import ssl
from email.message import EmailMessage

from config import SENDER_EMAIL, PASSWORD, RECEIVER_EMAIL_DICT

# christmas email sender function and template - start
def christmas_email_sender(receiver_name, festival_name):
    # message setting area
    message=EmailMessage()
    message['From'] = SENDER_EMAIL
    message['To'] = receiver_name
    message['Subject'] = festival_name
    # message.set_content(body)


    html = f"""
    <!DOCTYPE html>

<head>
	<title></title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml><![endif]-->
	<!--[if !mso]><!-->
	<link href="https://fonts.googleapis.com/css?family=Abril+Fatface" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Droid+Serif" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Oswald" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Roboto+Slab" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Merriweather" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Oxygen" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Permanent+Marker" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Nunito" rel="stylesheet" type="text/css">

</head>

<body style="background-color: #FFFFFF; margin: 0; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none;">
	<table class="nl-container" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #FFFFFF;">
		<tbody>
			<tr>
				<td>
					<table class="row row-1" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #f7f5f2;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-image: url('https://d1oco4z2z1fhwp.cloudfront.net/templates/default/696/christmas4_1.gif'); background-position: top center; background-repeat: no-repeat; color: #000000; width: 640px;" width="640">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="divider_block block-1" width="100%" border="0" cellpadding="20" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad">
																<div class="alignment" align="center">
																	<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																		<tr>
																			<td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 0px solid #BBBBBB;"><span>&#8202;</span></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
													<table class="text_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:25px;padding-left:10px;padding-right:10px;padding-top:10px;">
																<div style="font-family: Arial, sans-serif">
																	<div class style="font-size: 14px; font-family: 'Roboto Slab', Arial, 'Helvetica Neue', Helvetica, sans-serif; mso-line-height-alt: 16.8px; color: #555555; line-height: 1.2;">
																		<p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><span style="color:#ffffff;"><span style="font-size:18px;">?? December<span style="color:#c4b384;"><strong><span style> 25th</span></strong></span> ??</span><br></span></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
													<table class="image_block block-3" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="width:100%;padding-right:0px;padding-left:0px;">
																<div class="alignment" align="center" style="line-height:10px"><img class="big" src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/696/309fddd6-3e45-4125-a490-d88dbcde5939.png" style="display: block; height: auto; border: 0; width: 384px; max-width: 100%;" width="384" alt="Image" title="Image"></div>
															</td>
														</tr>
													</table>
													<table class="image_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="width:100%;padding-right:0px;padding-left:0px;">
																<div class="alignment" align="center" style="line-height:10px"><img class="big" src="https://freepngimg.com/save/19109-santa-claus-png-hd/336x359" style="display: block; height: auto; border: 0; width: 416px; max-width: 100%;" width="416" alt="Image" title="Image"></div>
															</td>
														</tr>
													</table>
													<table class="divider_block block-5" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-bottom:30px;padding-left:25px;padding-right:25px;padding-top:25px;">
																<div class="alignment" align="center">
																	<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																		<tr>
																			<td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 0px solid #BBBBBB;"><span>&#8202;</span></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
													<table class="text_block block-6" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:5px;padding-left:15px;padding-right:15px;padding-top:15px;">
																<div style="font-family: Tahoma, Verdana, sans-serif">
																	<div class style="font-size: 14px; font-family: 'Roboto', Tahoma, Verdana, Segoe, sans-serif; mso-line-height-alt: 21px; color: #555555; line-height: 1.5;">
																		<p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 21px;"><span style><span style="color:#333300;">By</span></span></p>
																		<p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 21px;"><span style><span style="color:#333300;">Abhijith KR</span></span></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-2" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #f7f5f2;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 640px;" width="640">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="divider_block block-1" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad">
																<div class="alignment" align="center">
																	<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																		<tr>
																			<td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 0px solid #BBBBBB;"><span>&#8202;</span></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					
				</td>
			</tr>
		</tbody>
	</table><!-- End -->
</body>

</html>

    """

    message.add_alternative(html, subtype="html")
    context=ssl.create_default_context() # it securing connection

    print(f'Sending Email to {receiver_name}')

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(SENDER_EMAIL, PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_name, message.as_string())

    print(f'{fest_name} wish sended to ', receiver_name)
# christmas email sender function and template - start   



# newyear email sender function and template - start
def newyear_email_sender(receiver_name, festival_name):
    # message setting area
    message=EmailMessage()
    message['From'] = SENDER_EMAIL
    message['To'] = receiver_name
    message['Subject'] = festival_name
    # message.set_content(body)


    html = f"""
	<!DOCTYPE html>
	<html xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en">

	<head>
		<title></title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet" type="text/css">
		<link href="https://fonts.googleapis.com/css?family=Permanent+Marker" rel="stylesheet" type="text/css">
		<link href="https://fonts.googleapis.com/css?family=Roboto+Slab" rel="stylesheet" type="text/css">
	</head>

	<body style="background-color: #000000; margin: 0; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none;">
		<table class="nl-container" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #000000;">
			<tbody>
				<tr>
					<td>
						<table class="row row-1" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-image: url('https://d1oco4z2z1fhwp.cloudfront.net/templates/default/186/ezgif-4-4ffef0a72c0c.gif'); background-position: top center; background-repeat: no-repeat;">
							<tbody>
								<tr>
									<td>
										<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;width: 100% !important;" width="650">
											<tbody>
												<tr>
													<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
														<table class="divider_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
															<tr>
																<td class="pad" style="padding-left:10px;padding-right:10px;padding-top:10px;">
																	<div class="alignment" align="center">
																		<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="20%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																			<tr>
																				<td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 2px dotted #E92C41;"><span>&#8202;</span></td>
																			</tr>
																		</table>
																	</div>
																</td>
															</tr>
														</table>
														<div class="spacer_block mobile_hide" style="height:30px;line-height:30px;font-size:1px;">&#8202;</div>
														<table class="text_block block-3" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
															<tr>
																<td class="pad" style="padding-top:20px;">
																	<div style="font-family: sans-serif">
																		<div class style="font-family: 'Permanent Marker', Impact, Charcoal, sans-serif; font-size: 12px; mso-line-height-alt: 14.399999999999999px; color: #E92C41; line-height: 1.2;">
																			<p style="margin: 0; text-align: center; font-size: 12px; mso-line-height-alt: 14.399999999999999px;"><span style="font-size:64px;">Happy</span></p>
																			<p style="margin: 0; text-align: center; font-size: 12px; mso-line-height-alt: 14.399999999999999px;"><span style="font-size:64px;">NEW YEAR</span></p>
																		</div>
																	</div>
																</td>
															</tr>
														</table>
														<table class="text_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
															<tr>
																<td class="pad">
																	<div style="font-family: Arial, sans-serif">
																		<div class style="font-family: 'Roboto Slab', Arial, 'Helvetica Neue', Helvetica, sans-serif; font-size: 12px; mso-line-height-alt: 14.399999999999999px; color: #FFFFFF; line-height: 1.2;">
																			<p style="margin: 0; text-align: center; font-size: 12px; mso-line-height-alt: 14.399999999999999px;"><span style="font-size:80px;"><strong><span style>{current_year.year+1}</span></strong></span></p>
																		</div>
																	</div>
																</td>
															</tr>
														</table>
													</td>
												</tr>
											</tbody>
										</table>
									</td>
								</tr>
							</tbody>
						</table>
						<table class="row row-2" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #FFFFFF; background-image: url('https://d1oco4z2z1fhwp.cloudfront.net/templates/default/186/fireworksbg_1.jpg'); background-position: top center; background-repeat: repeat;background-size: 1114px 370px;">
							<tbody>
								<tr>
									<td>
										<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;width: 100% !important;" width="650">
											<tbody>
												<tr>
													<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
														<table class="text_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
															<tr>
																<td class="pad" style="padding-bottom:10px;padding-left:10px;padding-right:10px;padding-top:300px;">
																	<div style="font-family: sans-serif">
																		<div class style="font-size: 12px; mso-line-height-alt: 18px; color: #000000; font-weight: bold; line-height: 1.5; font-family: Lato, Tahoma, Verdana, Segoe, sans-serif;">
																			<p style="margin: 0; font-size: 12px; text-align: center; mso-line-height-alt: 18px;">By</p>
																			<p style="margin: 0; font-size: 12px; text-align: center; mso-line-height-alt: 18px;">Abhijith KR</p>
																		</div>
																	</div>
																</td>
															</tr>
														</table>
													</td>
												</tr>
											</tbody>
										</table>
									</td>
								</tr>
							</tbody>
						</table>
						
					</td>
				</tr>
			</tbody>
		</table><!-- End -->
	</body>

	</html>
    """

    message.add_alternative(html, subtype="html")
    context=ssl.create_default_context() # it securing connection

    print(f'Sending Email to {receiver_name}')

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(SENDER_EMAIL, PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_name, message.as_string())

    print(f'{fest_name} wish sended to ', receiver_name)
# newyear email sender function and template - start 



# main area to check whether the festival fount - start
fest_name_data = {
                    'NewYear' : f'{current_year.year}-12-31', # 'NewYear' : '2023-01-01',
                    'RepublicDay' : f'{current_year.year}-01-26', 
                    'IndependenceDay' : f'{current_year.year}-08-15',
                    'GandhiJayanti' : f'{current_year.year}-10-02',  
                    'Christmas' : f'{current_year.year}-12-24', # 'Christmas' : '2022-12-25',
                }

for fest_name, day in fest_name_data.items():
    # print(fest_name, day)
    if date.today() == datetime.strptime(day, '%Y-%m-%d').date():
        # print('Trueee')
        if fest_name == 'NewYear':
            print('NewYear', day)
            for receiver_name in RECEIVER_EMAIL_DICT:
                # print(receiver_name)
                newyear_email_sender(receiver_name, 'Happy New Year!')

        elif fest_name == 'RepublicDay':
            print('RepublicDay', day)

        elif fest_name == 'IndependenceDay':
            print('IndependenceDay', day)

        elif fest_name == 'GandhiJayanti':
            print('GandhiJayanti', day)

        elif fest_name == 'Christmas':
            print('Christmas', day)
            for receiver_name in RECEIVER_EMAIL_DICT:
                # print(receiver_name)
                christmas_email_sender(receiver_name, 'Happy Christmas!')

    # else:
    #     print('No festival found on the date : ', date.today())


print('Completed.........!')